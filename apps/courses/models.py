from django.db import models
from apps.organization.models import CourseOrg,Teacher
from datetime import datetime

# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.CharField(verbose_name=u"课程详情",max_length=500)
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u"讲师", null=True, blank=True)
    degree = models.CharField(verbose_name=u"难度", choices=(("cj","初级"), ("zj","中级"), ("gj","高级")), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"课程类别")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name