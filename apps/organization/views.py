from django.shortcuts import render
from django.views import View
from .models import CourseOrg,CityDict
#分页
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class OrglistView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()
        all_cirys = CityDict.objects.all()
        org_nums = CourseOrg.objects.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(all_orgs,5,request=request)
        orgs = p.page(page)

        return render(request,"org-list.html",{"orgs":orgs,"citys":all_cirys,"org_nums":org_nums})