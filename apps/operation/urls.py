# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/2/20 15:04'

from django.urls import path,include,re_path
from apps.operation.views import UserAskView

urlpatterns = [
    path('add-ask/', UserAskView.as_view(),name="add-ask"),
]