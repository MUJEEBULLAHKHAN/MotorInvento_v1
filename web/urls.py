from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.homeview, name='home'),
    url(r'^register/$', views.registerview, name='register'),
    url(r'^login/$', views.loginview, name='login'),
    url(r'^dashboard/$', views.dashboardview, name='dashboard'),
    url(r'^landing/$', views.landview, name='landing'),
    url(r'^make/$', views.makeview, name='make'),
    url(r'^model/$', views.modelview, name='model'),
    url(r'^year/$', views.yearview, name='year'),
    url(r'^addcar/$', views.addcarview, name='addcar'),
    url(r'^addpart/$', views.addpartview, name='addpart'),
    url(r'^sellpart/$', views.sellpartview, name='sellpart'),
    url(r'^create_task/$', views.create_task, name='sellpart'),
]
