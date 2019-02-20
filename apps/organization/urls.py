from django.urls import path,include,re_path
from apps.organization.views import OrglistView,OrgDetailView,CourseDetailView

urlpatterns = [
    path('list/', OrglistView.as_view(),name="org-list"),
    path('org-base/', OrgDetailView.as_view()),
    re_path(r'org-course(?P<org_id>.*)/$',CourseDetailView.as_view(),name="org-course"),
]