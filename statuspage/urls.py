from django.conf import settings
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.views import login, logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, ListView, DetailView


admin.autodiscover()
urlpatterns = [
    re_path(r'^', include('status.urls', namespace='status')),
    re_path(r'^account/login/$', LoginView.as_view, {'template_name': 'admin/login.html'}, 'login'),
    re_path(r'^account/logout/$', LogoutView.as_view, {'template_name': 'admin/logout.html'}, 'logout'),
    re_path(r'^avatar/', include('avatar.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
]

app_name = 'status'

# if settings.DEBUG:
#     urlpatterns += url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT,
#     }),
#     urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]