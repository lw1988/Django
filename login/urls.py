from  django.conf.urls import  url
from . import views
from . import LoginController as  xixixi

urlpatterns=[
    url(r'login/',views.login),
    url(r'index/',views.index),
    url(r'register/',views.register),
    url(r'logout/',views.logout),
    url('function1/',xixixi.function1),
    url('function2/',xixixi.function2),
    url('function3/',xixixi.function3),
    url('function4/',xixixi.function4),


]