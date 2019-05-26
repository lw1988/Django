
from django.shortcuts import render
import pymysql

def connectDatabase():
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="1422127065",
        database="world",
        charset="utf8"
    )
    return con


#定义访问login.html的函数
def loginPage(request):
    if request.method=="POST":
        userName=request.POST.get("userName")
        userPasswd = request.POST.get("userPasswd")
        print("userName=", userName)
        print("userPasswd=", userPasswd)
        #屏蔽setting里第46行，也就是屏蔽python的拦截
        # login.html里面/login/代表urls里面的path,同一个目录
    return render(request,"login.html");
#在urls.py里定义路由访问

#测试图表
def echart(request):
    #x轴信息
    listx = ["java","嵌入式","前端"]
    #y轴信息
    listy = [300,200,100]
    #render多了一个传值参数
    return render(request,"echart.html",{"listx":listx,"listy":listy})

#户型-数量、户型-价格 --- 多柱形
def function4(request):
    if request.method == "POST":
        # 每个户型数量
        list = []
        con = connectDatabase();
        cur = con.cursor()
        sql1 = "select count(*) from lianjia WHERE zufang_type like '1室%'"
        cur.execute(sql1)
        resutl1 = cur.fetchone()
        print("result1=", resutl1)
        list.append(resutl1[0])

        sql2 = "select count(*) from lianjia WHERE zufang_type like '2室%'"
        cur.execute(sql2)
        resutl2 = cur.fetchone()
        print("result2=", resutl2)
        list.append(resutl2[0])

        sql3 = "select count(*) from lianjia WHERE zufang_type like '3室%'"
        cur.execute(sql3)
        resutl3 = cur.fetchone()
        print("result2=", resutl3[0])
        list.append(resutl3[0])

        sql4 = "select count(*) from lianjia WHERE zufang_type like '4室%'"
        cur.execute(sql4)
        resutl4 = cur.fetchone()
        print("result4=", resutl4[0])
        list.append(resutl4[0])

        sql5 = "select count(*) from lianjia WHERE zufang_type like '5室%'"
        cur.execute(sql5)
        resutl5 = cur.fetchone()
        print("result5=", resutl5)
        list.append(resutl5[0])

        sql6 = "select count(*) from lianjia WHERE zufang_type like '6室%'"
        cur.execute(sql6)
        resutl6 = cur.fetchone()
        print("result6=", resutl6)
        list.append(resutl6[0])

        list2 = []
        con = connectDatabase();
        cur = con.cursor()
        sql1 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '1室%'"
        cur.execute(sql1)
        resutl1 = cur.fetchone()
        print("result1=", resutl1)
        list2.append(resutl1[0])

        sql2 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '2室%'"
        cur.execute(sql2)
        resutl2 = cur.fetchone()
        print("result2=", resutl2)
        list2.append(resutl2[0])

        sql3 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '3室%'"
        cur.execute(sql3)
        resutl3 = cur.fetchone()
        print("result2=", resutl3[0])
        list2.append(resutl3[0])

        sql4 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '4室%'"
        cur.execute(sql4)
        resutl4 = cur.fetchone()
        print("result4=", resutl4[0])
        list2.append(resutl4[0])

        sql5 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '5室%'"
        cur.execute(sql5)
        resutl5 = cur.fetchone()
        print("result5=", resutl5)
        list2.append(resutl5[0])

        sql6 = "select AVG(del_house_price) from lianjia WHERE zufang_type like '6室%'"
        cur.execute(sql6)
        resutl6 = cur.fetchone()
        print("result6=", resutl6)
        list2.append(0)

        # y轴信息
        listy = ['1室', '2室', '3室', '4室', '5室', '6室']
        # x轴信息
        # listcount = [165, 170, 30, 165, 170, 30, 165, 170, 30, 200]
        # listprice = [150, 105, 110, 150, 105, 110, 150, 105, 110, 50]
        # #render多了一个传值参数
    return render(request, "function4.html", {'listy': listy, "list": list, "list2": list2})

#每个月的租房数量 --- 饼图
def function3(request):
    if request.method == "POST":
        con = pymysql.Connect(host="localhost", user="root", passwd="1422127065", database="world", charset="utf8")
        cursor = con.cursor()
        sql = "select publish_time,count(publish_time) from lianjia GROUP BY publish_time "
        cursor.execute(sql)
        result = cursor.fetchall()
        d = []
        for row in result:
            dic = {}
            dic['name'] = row[0]
            dic['value'] = row[1]
            d.append(dic)
        print("", result)
        cursor.close()
        con.close()
    return render(request, "function3.html", {'d': d})

#挂牌价-成交价-月份x的对应变化 ---多折线图
def function2(request):
    if request.method == "POST":
        con = pymysql.Connect(host="localhost", user="root", passwd="1422127065", database="world", charset="utf8")
        cursor = con.cursor()
        sql = "SELECT del_time, AVG(price),AVG (del_house_price) from lianjia  GROUP BY del_time "
        cursor.execute(sql)
        result = cursor.fetchall()
        # 月份
        m = []
        # 挂牌价
        listGua = []
        # 成交价
        listChu = []

        for x in result:
            m.append(x[0])
            listGua.append(str(x[1]).split('.')[0])
            listChu.append(str(x[2]).split('.')[0])
        cursor.close()
        con.close()
    return render(request, "function2.html", {'m': m, 'listGua': listGua, 'listChu': listChu})

#面积x对应的租房y的数量 --- 驯鹿
def function1(request):

        con = pymysql.Connect(host="localhost", user="root", passwd="1422127065", database="world", charset="utf8")
        cursor = con.cursor()
        sql = "select del_house_size,count(del_house_size) from lianjia GROUP BY del_house_size "
        cursor.execute(sql)
        result = cursor.fetchall()
        d1 = []
        d2 = []
        for row in result:
            d1.append(row[0])
            d2.append(row[1])
        print("", d1)
        print("", d2)
        cursor.close()
        con.close()
        return render(request, "function1.html", {'d1': d1, 'd2': d2})


