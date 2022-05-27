from django import forms
from .models import Question, Answer
from users.models import MyUser



class AskForm(forms.Form):

	title = forms.CharField(max_length=255, required=True)
	text = forms.CharField()

	def __init__(self, user,*args, **kwargs):

		self._user = user
		super(AskForm, self).__init__(*args, **kwargs)

	def save(self):

		self.cleaned_data['author'] = self._user

		return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):

	text = forms.CharField()

	def __init__(self, user, question,*args, **kwargs):

		self._user = user
		self._question = question
		super(AnswerForm, self).__init__(*args, **kwargs)

	def save(self):

		self.cleaned_data['question'] = self._question
		self.cleaned_data['author'] = self._user


		return Answer.objects.create(**self.cleaned_data)

