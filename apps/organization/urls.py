from django.urls import path,include,re_path
from apps.organization.views import OrglistView,OrgDetailView,CourseDetailView,OrgDescView,OrgTeacherView

urlpatterns = [
    path('list/', OrglistView.as_view(),name="org-list"),
    re_path(r'org-home(?P<org_id>.*)/$',OrgDetailView.as_view(),name="org-home"),
    re_path(r'org-course(?P<org_id>.*)/$',CourseDetailView.as_view(),name="org-course"),
    re_path(r'org-desc(?P<org_id>.*)/$',OrgDescView.as_view(),name="org-desc"),
    re_path(r'org-teacher(?P<org_id>.*)/$',OrgTeacherView.as_view(),name="org-teacher"),
]