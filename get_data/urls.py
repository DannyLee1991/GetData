from django.conf.urls import patterns, url
from views.index import index

urlpatterns = patterns('',
    url(r'^$',index),
    # url(r'^searchResult/$',searchResult),
    # url(r'^logList/$',logList),
    # url(r'^context/(.*)$',context),
    # url(r'^feedback/$',feedback),
    # url(r'^logDetail/$',logDetail),
    # url(r'^choose/$',choose),
    # url(r'^manage/$',manage),
)