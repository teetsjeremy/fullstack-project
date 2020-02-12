from django.conf.urls import url
from .views import patterns


urlpatterns = [
    url(r'^$', patterns, name='patterns')
    ]