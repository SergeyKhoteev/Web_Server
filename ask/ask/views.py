from django.http import HttpResponse
from django.shortcuts import render
from qa.models import Question


def new_questions(request):

    question_list = Question.objects.new()

    context = {'print_list': question_list}

    template = 'qa/templates/blank_template.html'

    return render(request, template, context)


# Create your views here.
