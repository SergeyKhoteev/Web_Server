from django import forms
from .models import Question, Answer



class AskForm(forms.Form):

	title = forms.CharField(max_length=255, required=True)
	text = forms.CharField()

	def save(self):

		question = Question(**self.cleaned_data)
		question.save()

		return question


class AnswerForm(forms.Form):

	text = forms.CharField()
	question = forms.ModelChoiceField(queryset=Question.objects.all())

	def save(self):

		answer = Answer(**self.cleaned_data)
		print(answer)
		answer.save()

		return answer

	# def clean_text(self):

	# 	text = self.cleaned_data['text']
	# 	answers = Answer.objects.all()

	# 	for answer in answers:
	# 		if answer.text == text:
	# 			raise forms.ValidationError(
	# 				'Answer already exists')

