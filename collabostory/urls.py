from django.conf.urls import patterns, url

from collabostory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<story_id>\d+)/$', views.story, name='story'),
    url(r'^addstory/$', views.addstory, name='addstory'),
    url(r'^upvote/$', views.upvote, name='upvote'),
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^(?P<story_id>\d+)/add/$', views.add, name='add'),
    url(r'^searchstory/$', views.searchstory, name='searchstory'),
    url(r'^(?P<search_param>\w+)/$', views.index, name='index'),
)