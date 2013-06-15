from django.conf.urls import patterns, url

from collabostory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<story_id>\d+)/$', views.story, name='story'),
    url(r'^(?P<story_id>\d+)/add/$', views.add, name='add'),
)