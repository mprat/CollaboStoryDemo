from django.conf.urls import patterns, url

from collabostory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)