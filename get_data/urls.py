from django.conf.urls import patterns, url
from views.index import index
from views.price_ranking import price_ranking
from views.spider import spider

urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^price_ranking$',price_ranking),
    url(r'^spider$',spider),
)