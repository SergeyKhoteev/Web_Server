from django.urls import path, re_path

from qa.views import question_page, pop_questions, add_question_page, new_questions

urlpatterns = [

    path('new/', new_questions, name='new_questions'),
	path('question/<int:pk>/', question_page, name='question_page'),
	path('popular/', pop_questions, name='pop_questions'),
    path('ask/', add_question_page, name='add_question_page'),
]
