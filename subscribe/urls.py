from django.conf.urls import url
from .views import create_subscribe


urlpatterns = [
    url(r'^$', create_subscribe, name='create_subscribe')
    ]