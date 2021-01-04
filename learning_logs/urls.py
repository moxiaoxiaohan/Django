'''定义learning_logs的URL模式'''

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    #主页
    re_path(r'^$', views.index, name='index') ,
    #显示所有主题
    re_path(r'^topics/$', views.topics, name='topics'),
    #显示特定主题的详细页面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    #用于编辑主题
    #re_path(r'^topics/(?P<topic_id>\d+)/edit_topic/$', views.edit_topic, name='edit_topic'),
    re_path(r'^edit_topic/(?P<topic_id>\d+)/$', views.edit_topic, name='edit_topic'),
    #用于添加新的条目页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    #用于删除主题
    re_path(r'^delete_topic/(?P<topic_id>\d+)/$', views.delete_topic, name='delete_topic'),
    #用于删除条目
    re_path(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),


]

app_name = 'learning_logs'
