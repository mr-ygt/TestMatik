from django.conf.urls import url
from .views import *

app_name = 'soru'

urlpatterns = [
    url(r'^index/$', soru_index, name='index'),
    url(r'^myindex/$', my_index, name='myindex'),
    url(r'^testindex/$', soru_testindex, name='testindex'),
    url(r'^create/$', soru_create, name='create'),
    url(r'^pdf/$', GeneratePdf.as_view(), name='pdf'),

    url(r'^(?P<slug>[\w-]+)/$', soru_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', soru_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', soru_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/settest/$', soru_settest, name='settest'),
    url(r'^(?P<slug>[\w-]+)/quittest/$', soru_quittest, name='quittest'),
]