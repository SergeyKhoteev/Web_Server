from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from datetime import datetime, timedelta

from ask.views import MainMenu, SideMenu
from users.models import Session
from users.forms import SignUpForm, LogInForm
from qa.models import Question
from portfolios.models import UserPortfolio

# Create your views here.


def user_page(request, username):

	if not request._user:
		return redirect(reverse('login'))
	if request._user.username != username:
		raise PermissionDenied

	my_questions = Question.objects.filter(author=request._user)
	my_portfolios = UserPortfolio.objects.filter(Owner=request._user)

	context = {
	'User': request._user,
	'Questions': my_questions,
	'Portfolios': my_portfolios,
	'MainMenu': MainMenu,
	'SideMenu': SideMenu,
	}

	return render(
	request,
	'users/userpage_template.html',
	context
	)


