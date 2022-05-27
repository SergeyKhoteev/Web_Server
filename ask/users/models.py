from django.db import models
import random
import string
import datetime
from django.utils import timezone


# Create your models here.

class MyUser(models.Model):

	username = models.CharField(max_length=255, null=True, blank=False, unique=True)
	email = models.EmailField(max_length=254, null=True, blank=False)
	password = models.CharField(max_length=255, null=True, blank=False)

	def __str__(self):

		return self.username


class Session(models.Model):

	user = models.OneToOneField('MyUser', on_delete=models.CASCADE, null=True)
	session_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
	expire_date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)


	def generate_session_id(self):

		letters = string.ascii_letters + string.digits 
		session_id = (''.join(random.choice(letters) for i in range(245)))
		self.session_id = session_id

		# timezone.now()
		expire_date = timezone.now() + datetime.timedelta(days=2)
		self.expire_date = expire_date

		self.save()


