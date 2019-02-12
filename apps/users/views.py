from django.shortcuts import render
from django.views import View
from .forms import LoginForm,RegisterForm,ForgetPasswordForm,ResetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.backends import ModelBackend
from apps.users.models import UserProfile,EmailVerifyRecord
from django.db.models import Q
#加密
from django.contrib.auth.hashers import make_password
#发送电子邮件
from utils.email_send import send_register_email
# Create your views here.

#登陆view
class LoginViews(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get("username","")
                pass_word = request.POST.get("password","")
                #用户名密码验证
                user = authenticate(username=user_name,password=pass_word)
                if user is not None:
                  if user.is_active:
                      #用户登陆
                      login(request,user)
                      return render(request,"index.html")
                  else:
                      return render(request,"login.html",{"msg":"用户未激活"})
                else:
                  return render(request,"login.html",{"msg":"用户名或密码错误"})
            else:
                return render(request,"login.html",{"login_form":login_form})

class IndexView(View):
    def get(self,request):
        return render(request,'index.html',{})

#重载验证用户登陆的类，实现用户名和邮箱都可登陆
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#用户注册view
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email","")
            pass_word = request.POST.get("password","")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            #向用户填写的邮箱发送激活邮件
            send_register_email(user_name,"register")
            return render(request,"login.html",{"msg":"请进入邮箱激活账户"})
        else:
            return render(request,'register.html',{"msg":"请进入邮箱激活账户"})

#用户激活view
class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return render(request,'login.html')


class ForgetPasswordView(View):
    def get(self,request):
        forget_password_form = ForgetPasswordForm()
        return render(request, 'forgetpwd.html',{'forget_password_form':forget_password_form})

    def post(self,request):
        #forget_password_form = ForgetPasswordForm()
        #forget_password_form.username = request.POST.get("email","")
        email = request.POST.get("email", "")
        all_records = UserProfile.objects.filter(email=email)
        if all_records :
            for record in all_records:
                send_register_email(email,"forget")
                return render(request,'forgetpwd.html',{"msg":"请登陆邮箱完成验证"})
        else:
            return render(request,'forgetpwd.html',{"msg":"用户不存在！"})

class ResetPasswordView(View):
    def get(self,request,reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request,"password_reset.html",{"email":email})
        else:
            return render(request,"forgetpwd.html",{"msg":"链接不存在"})

class PasswordModifyView(View):
    def post(self,request):
        email = request.POST.get("email","")
        all_records = UserProfile.objects.filter(email = email)
        if all_records:
            for record in all_records:
                password1 = request.POST.get("password1","")
                password2 = request.POST.get("password2", "")
                if password1 == password2:
                    record.password = make_password(password=password2)
                    record.save()
                    verify_record = EmailVerifyRecord.objects.filter(email = email)
                    for record in verify_record:
                        record.delete()
                    return render(request, "login.html",{"msg":"重置成功，请登陆！"} )
                else:
                    return render(request,"password_reset.html",{"msg":"密码不一致！"})
        else:
            return render(request,"password_reset.html",{"msg":"用户名不存在！"})


