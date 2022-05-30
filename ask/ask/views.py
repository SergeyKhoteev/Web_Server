from django.http import HttpResponse
from django.shortcuts import render

MainMenu = {
	'Sign Up': 'signup',
	'Log In': 'login',
	'Log Out': 'logout'
}

SideMenu = {
	'New Questions': 'new_questions',
	'Popular Questions': 'pop_questions',
	'Add Question': 'add_question_page',
}