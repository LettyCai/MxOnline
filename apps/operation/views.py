from django.shortcuts import render
from django.views import View
from .models import UserAsk

# Create your views here.
class UserAskView(View):
    def post(self,request):
        user_ask_form = UserAsk(request.POST)
        if user_ask_form.valid():
            user_ask = user_ask_form.save(commit=True)

        pass
