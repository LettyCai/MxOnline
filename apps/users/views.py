from django.shortcuts import render
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class LoginViews(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.isvalid():
            user_name = request.POST.get("username","")
            pass_word = request.POST.get("password","")
            user = authenticate(username=user_name,password=pass_word)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("login"))
            else:
                return render(request,"login.html",{"msg":"用户名或密码错误"})
        else:
            return render(request,"login.html",{"login_form":login_form})

