from django.shortcuts import render
from django.views import View
from operation.forms import UserAskForm
from django.http import HttpResponse

# Create your views here.
#用户添加咨询
class UserAskView(View):
    def post(self,request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            user_ask = user_ask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"',content_type='application/json')
