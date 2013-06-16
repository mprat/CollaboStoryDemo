# Create your views here.
from django.shortcuts import render, get_object_or_404
from collabostory.models import Story, Sentence
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request, search_param=""):
	# list all the stories in alphabetical order by title
	stories_list = []
	if (search_param==""):
		stories_list = Story.objects.order_by('id')
	else:
		stories = Story.objects.all()
		for story in stories:
			if search_param.lower() in story.title.lower():
				stories_list.append(story)
	context = {'stories_list': stories_list}
	return render(request, 'collabostory/index.html', context)

def story(request, story_id):
	# list all the sentences in order by id
	story = Story.objects.get(id=story_id)
	story_title = story.title
	sentences = story.sentence_set.all()
	context = {'sentences': sentences, 'story_title': story_title, 'story': story}
	return render(request, 'collabostory/story.html', context)

def add(request, story_id):
	# s = get_object_or_404(Story, pk=story_id)
	# add in try / catch for not adding a blank sentence
	new_sentence = request.POST['next_sentence']
	s = Sentence(story=Story.objects.get(id=story_id), text=new_sentence)
	s.save()
	return HttpResponseRedirect(reverse('collabostory:story', args=(story_id, )))

def addstory(request):
	s = Story(title=request.POST['title'])
	s.save()
	return HttpResponseRedirect(reverse('collabostory:story', args=(s.id, )))

def searchstory(request):
	title_comp = request.POST['title_val']
	if title_comp=="":
		return HttpResponseRedirect(reverse('collabostory:index'))
	else:
		return HttpResponseRedirect(reverse('collabostory:index', args=(title_comp, )))

def upvote(request):
	story_id = request.POST['story_id']
	story = Story.objects.get(id=story_id)
	story.upvotes += 1
	story.save()
	return HttpResponseRedirect(reverse('collabostory:story', args=(story_id, )))

def downvote(request):
	story_id = request.POST['story_id']
	story = Story.objects.get(id=story_id)
	story.downvotes += 1
	story.save()
	return HttpResponseRedirect(reverse('collabostory:story', args=(story_id, )))
