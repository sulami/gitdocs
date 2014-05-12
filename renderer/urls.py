from django.conf.urls import patterns, include, url
from renderer.views import *

urlpatterns = patterns('renderer.views',
    url(r'^$', 'index', name='index'),
    url(r'(?P<username>[\w]+)/(?P<reponame>[\w]+)/(?P<versionname>[\w]+)/$',
        'version', name='version'),
    url(r'(?P<username>[\w]+)/(?P<reponame>[\w]+)/$', 'repo', name='repo'),
)

