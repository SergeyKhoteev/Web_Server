from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):

	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-rating')


class Question(models.Model):
	title = models.CharField(max_length=255, default='Question without name')
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	rating = models.IntegerField(null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	likes = models.ManyToManyField(User, related_name='likes')

	objects = models.Manager()
	question_manager = QuestionManager()

	def __str__(self):
		return self.title


class Answer(models.Model):
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title
