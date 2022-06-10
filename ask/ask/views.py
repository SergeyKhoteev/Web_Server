from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from users.forms import SignUpForm, LogInForm
from django.urls import reverse
from users.models import Session

from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

# MainMenu = {
# 	'Sign Up': 'signup',
# 	'Log In': 'login',
# 	'Log Out': 'logout'
# }

MainMenu = {'user': {
				'Log Out': 'logout'},
			'no_user': {
				'Sign Up': 'signup',
				'Log In': 'login',}
			}


SideMenu = {
	# 'Questions': 'new_questions',
	# 'Popular Questions': 'pop_questions',
	# 'Add Question': 'add_question_page',
	# 'Indexes': 'indexes_start_page',
	'Add portfolio': 'new_portfolio',
}

def signup(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		url = '/questions/'
		if form.is_valid():
			session = form.save_and_login_user()
			if session:
				response = HttpResponseRedirect(url)
				response.set_cookie(
					'sessionid', 
					session.session_id, 
					expires=session.expire_date, 
					httponly=True
					)
				return response
	else:
		form = SignUpForm()

	context = {
	'form': form,
	'MainMenu': MainMenu,
	'SideMenu': SideMenu,
	'PageName': "Sign Up"
	}

	return render(
		request,
		'users/signup.html',
		context)


def login(request):
	if request.method == 'POST':
		form = LogInForm(request.POST)
		if form.is_valid():
			session = form.do_login()
			if session:
				url = session.user.get_absolute_url()
				response = HttpResponseRedirect(url)
				response.set_cookie(
					'sessionid', 
					session.session_id, 
					expires=session.expire_date, 
					httponly=True
					)
				return response
	else:
		form = LogInForm()

	context = {
	'form': form,
	'MainMenu': MainMenu,
	'SideMenu': SideMenu,
	'PageName': "Log In"
	}

	return render(
		request,
		'users/login.html',
		context)


def logout(request):

	sessid = request.COOKIES.get('sessionid', None)

	if sessid is not None:
		session = Session.objects.get(session_id=sessid)
		expire_date = timezone.now() - timedelta(days=3)

		url = '/questions/new'
		response = HttpResponseRedirect(url)
		response.set_cookie(
			'sessionid',
			session.session_id,
			expires = expire_date)

		session.delete()

		return(response)
	
	else:
		return HttpResponseRedirect('/questions/new')