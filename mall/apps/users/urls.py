# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: Robinson_Jim
# @time: 18-8-19 下午7:23
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^usernames/(?P<username>\w{5,20})/count/',views.RegisterUsernameView.as_view(),name='usernamecount'),
]