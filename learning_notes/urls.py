"""定义learning_notes的URL模式"""
from django.urls import re_path

from . import views
app_name = 'learning_notes'
urlpatterns = [
    # 主页
    re_path('^$', views.index, name='index'),
]

