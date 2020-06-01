from django.conf.urls import url
from .views import *

app_name = 'soru'

urlpatterns = [
    url(r'^index/$', soru_index, name='index'),
    url(r'^create/$', soru_create, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', soru_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', soru_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', soru_delete, name='delete'),
]