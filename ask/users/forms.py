from django import forms
from .models import MyUser, Session
from django.db.utils import IntegrityError
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):

	class Meta:

		model = MyUser
		fields = ['username', 'email', 'password']

	def clean_password(self):
		if self.data.get('username') == self.data.get('password'):
			print('valid error')
			raise ValidationError(
				_('Change your passord. Password cannot be the same as username.'))	
		else:
			return self.cleaned_data.get('password')

	def save_and_login_user(self):

		user = MyUser(**self.cleaned_data)
		user.save()
		session = Session(user=user)
		session.generate_session_id()
		session.save()

		return session


class LogInForm(forms.Form):

	username = forms.CharField(max_length=255, required=True)
	password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput())

	def clean(self):
		try:
			user = MyUser.objects.get(username = self.cleaned_data.get('username'))
			if user.password != self.cleaned_data.get('password'):
				raise ValidationError(
					_('Wrong login/password')
					)
		except:
			raise ValidationError(
				_('Wrong login/password')
				)


	def do_login(self):
		username = self.cleaned_data.get('username')
		user = MyUser.objects.get(username=username)
		session, created = Session.objects.get_or_create(user=user)
		session.generate_session_id()

		return session