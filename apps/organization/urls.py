from django.urls import path,include,re_path
from apps.organization.views import OrglistView

urlpatterns = [
    path('list/', OrglistView.as_view(),name="org-list"),
]