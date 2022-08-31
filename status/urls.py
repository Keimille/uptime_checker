from django.urls import re_path, include
from django.views.decorators.cache import cache_page
from tastypie.api import NamespacedApi
from status.api import IncidentResource, StatusResource
from status.models import Incident
from status.views import (
    DashboardView, HomeView, IncidentArchiveMonthView, IncidentArchiveYearView, IncidentDeleteView,
    IncidentDetailView, IncidentUpdateUpdateView, create_incident, IncidentHideView, HiddenDashboardView
)


v1_api = NamespacedApi(api_name='v1', urlconf_namespace='status')
v1_api.register(StatusResource())
v1_api.register(IncidentResource())


urlpatterns = [
    re_path(r'^api/', include(v1_api.urls)),
    re_path(r'^$', cache_page(15)(HomeView.as_view()), name='home'),
    re_path(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    re_path(r'^dashboard/hidden/$', HiddenDashboardView.as_view(), name='dashboard_hidden'),
    re_path(r'^incident/new/$', create_incident, name='incident_create'),
    re_path(r'^incident/(?P<pk>\d+)/$', IncidentDetailView.as_view(model=Incident), name='incident_detail'),
    re_path(r'^incident/(?P<pk>\d+)/update/$', IncidentUpdateUpdateView.as_view(), name='incident_update'),
    re_path(r'^incident/(?P<pk>\d+)/hide/$', IncidentHideView.as_view(), name='incident_hide'),
    re_path(r'^incident/(?P<pk>\d+)/delete/$', IncidentDeleteView.as_view(), name='incident_delete'),
    re_path(r'^archive/(?P<year>\d{4})/$', IncidentArchiveYearView.as_view(), name="archive_year"),
    re_path(
        r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$',
        IncidentArchiveMonthView.as_view(month_format='%m'),
        name="archive_month_numeric"
    ),
]

app_name = 'status'