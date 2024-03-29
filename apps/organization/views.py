from django.shortcuts import render
from django.views import View
from .models import CourseOrg,CityDict,Teacher
from apps.courses.models import Course
#分页
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class OrglistView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_cirys = CityDict.objects.all()

        #热门机构
        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        #取出筛选城市
        city_id = request.GET.get('city',"")
        if city_id :
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #取出筛选机构类型
        org_ct = request.GET.get('ct',"")
        if org_ct :
            all_orgs =all_orgs.filter(category=org_ct)

        org_nums = all_orgs.count()

        sort = request.GET.get('sort',"")
        if sort :
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            if sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")




        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs,5,request=request)
        orgs = p.page(page)

        return render(request,"org-list.html",{
            "orgs":orgs,
            "citys":all_cirys,
            "org_nums":org_nums,
            "city_id":city_id,
            "org_ct":org_ct,
            "hot_orgs":hot_orgs,
            "sort":sort})

class OrgDetailView(View):
    def get(self,request,org_id):

        if org_id :
            courses = Course.objects.filter(course_org=org_id)[:3]

            teachers = Teacher.objects.filter(org_id=org_id)[:3]

            orgs = Course.objects.filter(course_org=org_id)
            for org in orgs:
                desc = org.desc

        return render(request,"org-detail-homepage.html",{"teachers":teachers,"courses":courses,"desc":desc,"org_id":org_id})

class CourseDetailView(View):
    def get(self,request,org_id):
        if org_id:
            courses = Course.objects.filter(course_org=org_id)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(courses,3,request=request)
        courses = p.page(page)

        return render(request,"org-detail-course.html",{"courses":courses,"org_id":org_id})

class OrgDescView(View):
    def get(self,request,org_id):
        if org_id:
            orgs = Course.objects.filter(course_org=org_id)
            for org in orgs:
                desc = org.desc
            return render(request,"org-detail-desc.html",{"desc":desc,"org_id":org_id})
        else:
            pass

class OrgTeacherView(View):
    def get(self,request,org_id):
        if org_id:
            teachers = Teacher.objects.filter(org_id=org_id)

        return render(request,"org-detail-teachers.html",{"teachers":teachers,"org_id":org_id})