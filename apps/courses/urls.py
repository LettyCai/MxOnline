from django.urls import path,include,re_path
from apps.courses.views import CourseListView

urlpatterns = [
    path('course-list/', CourseListView.as_view(),name="course-list"),
    re_path(r'org-home(?P<org_id>.*)/$',CourseListView.as_view(),name="org-home"),
]