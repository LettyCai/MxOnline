from django.contrib import admin
from .models import CourseOrg,CityDict
# Register your models here.
class CourseOrgAdmin(admin.ModelAdmin):
    pass

admin.site.register(CourseOrg,CourseOrgAdmin)

class CityDictAdmin(admin.ModelAdmin):
    pass

admin.site.register(CityDict,CityDictAdmin)
