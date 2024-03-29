from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_user = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birthday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender = models.CharField(max_length=8,choices=(('male',u'男'),('female',u'女')),default='female')
    address = models.CharField(max_length=100,verbose_name=u'地址',default='')
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y/%M',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.username

class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型",
                                 choices=(("register", u"注册"), ("forget", u"找回密码"), ("update_email", u"修改邮箱")),
                                 max_length=30)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
