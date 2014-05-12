from django.conf.urls import patterns, include, url
from renderer.views import *

urlpatterns = patterns('renderer.views',
    url(r'^$', 'index', name='index'),
)

