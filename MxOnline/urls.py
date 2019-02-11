"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include,re_path
from apps.users.views import LoginViews,IndexView,RegisterView,ActiveUserView
from django.contrib import admin

urlpatterns = [
    path('',  IndexView.as_view(),name="index"),
    path('xadmin/', admin.site.urls),
    path('login/', LoginViews.as_view(),name="login"),
#    path('index/', IndexView.as_view(),name="index"),
    path('register/', RegisterView.as_view(),name="register"),
    path(r'^captcha/', include('captcha.urls')),
    re_path(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name="active_user")
#example    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
]