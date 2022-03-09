from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	title = models.CharField('deafault title', max_length=255, null=True)
	text = models.TextField(blank=False, null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	# rating = models.IntegerField(null=True)
	# author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	# likes = models.ManyToManyField(User)


class Answer(models.Model):
	text = models.TextField(null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


# class Question_has_like(models.Model):
# 	question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
# 	user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)



class Answer2(models.Model):
	text = models.TextField(null=True)
	added_at = models.DateTimeField(auto_now_add=True, null=True)
	question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

