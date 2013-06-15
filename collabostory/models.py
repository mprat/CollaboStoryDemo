from django.db import models

class Story(models.Model):
	# sentences = models.ManyToManyField(Sentence)
	title = models.CharField(max_length=300)

	def __unicode__(self):
		return self.title

class Sentence(models.Model):
	story = models.ForeignKey(Story)
	text = models.TextField()

	def __unicode__(self):
		return self.text
