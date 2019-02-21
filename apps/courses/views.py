from django.shortcuts import render
from django.views import View
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class CourseListView(View):
    def get(self,request):
        courses = Course.objects.all()
        hot_courses = courses.order_by("-click_nums")[:3]

        sort = request.GET.get('sort',"")

        if sort:
            if sort == "hot":
                courses = courses.order_by("-click_nums")
            if sort == "students":
                courses = courses.order_by("-students")

        #对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(courses,9,request=request)
        courses = p.page(page)

        return render(request,"course-list.html",{"courses":courses,"sort":sort,"hot_courses":hot_courses})



