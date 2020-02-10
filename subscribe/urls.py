from django.conf.urls import url, include
from .views import create_subscribe


urlpatterns = [
    url(r'^$', create_subscribe, name='subscribe')
]