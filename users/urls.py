'''为应用程序users定义URL模式'''
from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    #登陆页面
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', views.logout_view, name='logout'),
    re_path(r'^register/$', views.register, name='register'),

]

app_name = 'users'