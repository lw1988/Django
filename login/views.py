from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
from . import models
# Create your views here.
def index(request):
    return  render(request,"login/index.html")
def login(request):
    #不允许重复登录
    if request.session.get('is_login',None):
        return  redirect('/index')
    if request.method=="POST":
        login_form=forms.UserForm(request.POST)
        #locals()返回当前所有的本地变量字典
        message="请检查填写的内容"
        if login_form.is_valid():
            username=login_form.cleaned_data["username"]
            password=login_form.cleaned_data["password"]
            try:
                user=models.User.objects.get(username=username)
                if user.password==password:
                    #将用户的转态和数据写入session字典
                    request.session['is_login']=True
                    request.session['user_id']=user.id
                    request.session['user_name']=user.username
                    return redirect("/index/")
                else:
                    message="密码错误"
            except:
                message="用户不存在"
        return  render(request,"login/login.html",locals())
    login_form=forms.UserForm()
    return  render(request,'login/login.html',locals())
def register(request):
   if request.session.get('is_login',None):
       return  redirect('/index/')
   if request.method=="POST":
       register_form=forms.RegisterForm(request.POST)
       message="请检查填写的内容是否有误"
       if register_form.is_valid():#数据获取
           username=register_form.cleaned_data['username']
           password1=register_form.cleaned_data['password1']
           password2=register_form.cleaned_data['password2']
           email=register_form.cleaned_data['email']
           sex=register_form.cleaned_data['sex']
           print(username+"--"+password1)
           if password1!=password2==False:
               message="两次输入的密码不一致"
               return  render(request,'login/register.html',locals())
           else:
               user_name=models.User.objects.filter(username=username)
               if user_name:
                   message="用户名重复"
                   return  render(request,'login/register.html',locals())
               user_email=models.User.objects.filter(email=email)
               if user_email:
                   message="邮箱已注册"
                   return render(request, 'login/register.html',locals())
               new_user=models.User()
               new_user.username=username
               new_user.password=password1
               new_user.sex=sex
               new_user.email=email
               new_user.save()
               return redirect('/login/')

   register_form=forms.RegisterForm()
   return  render(request,'login/register.html',locals())
def logout(request):
    if not request.session.get('is_login',None):
        return  redirect('/index/')
    request.session.flush()#退出时清理session里的所有内容
    return  redirect('/index/')