from django.conf.urls import url
from .views import index, patterns


urlpatterns = [
    url(r'^$', patterns, name='patterns'),
    url(r'^index/$',index, name='index')
    ]