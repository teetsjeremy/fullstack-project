from django.conf.urls import url
from .views import patterns
from .views import get_patterns


urlpatterns = [
    url(r'^$', patterns, name='patterns'),
    url(r'^$', get_patterns, name='get_patterns')
    ]