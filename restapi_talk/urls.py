from django.conf.urls import patterns, include, url
from django.contrib import admin
from restapi_talk import api

admin.autodiscover()
api.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/', include(api.v1_api.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
