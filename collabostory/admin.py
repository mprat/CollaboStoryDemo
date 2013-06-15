from django.contrib import admin
from collabostory.models import Story, Sentence

class SentencesInline(admin.StackedInline):
	model=Sentence
	extra=2

class StoryAdmin(admin.ModelAdmin):
	fields = ['title']
	inlines = [SentencesInline]

admin.site.register(Story, StoryAdmin)