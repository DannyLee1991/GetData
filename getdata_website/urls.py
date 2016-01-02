from django.conf.urls import include, url, patterns
from django.contrib import admin
import get_data.urls
import settings

urlpatterns = patterns('',
    url(r'^', include(get_data.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_URL})
)