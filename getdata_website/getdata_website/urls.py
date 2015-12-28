from django.conf.urls import include, url, patterns
from django.contrib import admin
import get_data.urls

urlpatterns = patterns('',
    url(r'^', include(get_data.urls)),
    url(r'^admin/', include(admin.site.urls)),
)