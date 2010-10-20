from django.conf.urls.defaults import *


urlpatterns = patterns('',

    (r'^$', 'googlesearch.views.googlesearch'), 
)