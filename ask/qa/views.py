from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from qa.models import Question
from qa.forms import AskForm, AnswerForm
from ask.views import MainMenu, SideMenu
from users.models import Session 


def index(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the polls index.")


def new_questions(request):

    question_list = Question.objects.new()
    paginator = Paginator(question_list, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
    'User': request._user,
    'MainMenu': MainMenu,
    'SideMenu': SideMenu,
    'q_list': page_obj,
    'PageName': "New Questions"
    }

    return render(request, 'new_question_template.html', context)


def pop_questions(request):

    question_list = Question.objects.popular()
    paginator = Paginator(question_list, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
    'User': request._user,
    'MainMenu': MainMenu,
    'SideMenu': SideMenu,
    'q_list': page_obj,
    'PageName': "Popular Questions"
    }

    return render(request, 'pop_question_template.html', context)


def question_page(request, pk):

    try:
        question = Question.objects.get(pk=pk)
        answers = question.answer_set.all()

        if request.method == 'POST':
            if not request._user:
                return redirect(reverse('login'))
            form = AnswerForm(request._user, question, request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('question_page',kwargs={'pk': question.pk} ))
        else:
            form = AnswerForm(request._user, question)

        context = {
        'User': request._user,
        'question': question,
        'answers': answers,
        'form': form,
        'MainMenu': MainMenu,
        'SideMenu': SideMenu,
        'PageName': question.title
        }

    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_page_template.html', context)


def add_question_page(request):

    if not request._user:
        return(redirect(reverse('login')))

    if request.method == 'POST':
        form = AskForm(request._user, request.POST)
        if form.is_valid():
            try:
                question = form.save()
                url = question.get_absolute_url()
                return HttpResponseRedirect(url)
            except:
                form.add_error(None, 'Failed to create question')
    else:
        form = AskForm(request._user)

    context = {
        'User': request._user,
        'form': form,
        'MainMenu': MainMenu,
        'SideMenu': SideMenu,
        'PageName': 'Add new question'
        }
    
    return render(request, 'add_question_template.html', context)