from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, LogInForm
from django.urls import reverse
from ask.views import MainMenu, SideMenu

from datetime import datetime, timedelta

# Create your views here.


def signup(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		url = request.POST.get('continue', '/')
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
		url = request.POST.get('continue', '/')
		if form.is_valid():
			session = form.do_login()
			if session:
				response = HttpResponseRedirect(url)
				response.set_cookie(
					'sessionid', 
					session.session_id, 
					expires=session.expire_date, 
					httponly=True
					)
				print(session.session_id)
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