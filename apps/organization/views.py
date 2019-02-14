from django.shortcuts import render
from django.views import View
from apps.organization.models import CityDict,CourseOrg
# Create your views here.

class OrglistView(View):
    def get(self,request):
        all_orgs = CourseOrg.objects.all()

        
        return render(request,"base.html")