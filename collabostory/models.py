from django.db import models

class Sentence(models.Model):
	text = models.TextField()

	def __unicode__(self):
		return self.text

class Story(models.Model):
	sentences = models.ManyToManyField(Sentence)
	title = models.CharField(max_length=300)

	def __unicode__(self):
		return self.title