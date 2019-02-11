# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/2/10 19:56'
from apps.users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

def send_register_email(email,type="register"):
    email_record = EmailVerifyRecord()
    random_str = generater_random_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = type
    email_record.save()

    email_title = ""
    email_body = ""

    if type == "register":
        email_title = "This is an active email:"
        email_body = "Please click this link to active your account : http://127.0.0.1:8000/active/{0}".format(random_str)
        email_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if email_status == True:
            pass



def generater_random_str(random_length=8):
    str = ''
    chars = 'QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq1234567890'
    length = len(chars)-1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str