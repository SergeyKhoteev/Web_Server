from django.db import models
from users.models import MyUser


class QuestionManager(models.Manager):

	def new(self):
		return self.order_by('-added_at')

	def popular(self):
		return self.order_by('-rating')


class Question(models.Model):
	title = models.CharField(max_length=255, default='Question without name')
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
	likes = models.ManyToManyField(MyUser, related_name='likes')

	objects = QuestionManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('question_page', kwargs={'pk': self.id})


class Answer(models.Model):
	text = models.TextField(blank=True, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	question = models.ForeignKey('Question', on_delete=models.CASCADE, null=True)
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.text
