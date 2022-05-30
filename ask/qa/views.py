from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from qa.models import Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AskForm, AnswerForm
from django.urls import reverse
from ask.views import MainMenu, SideMenu
from users.models import Session 


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new_questions(request):

    sessid = request.COOKIES.get('sessionid', None)

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
    # 'User': user,
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
    'MainMenu': MainMenu,
    'SideMenu': SideMenu,
    'q_list': page_obj,
    'PageName': "Popular Questions"
    }

    return render(request, 'pop_question_template.html', context)


def question_page(request, pk):

    sessid = request.COOKIES.get('sessionid', None)
    if sessid:
        session = Session.objects.get(session_id=sessid)
        user = session.user
    else:
        return redirect(reverse('login'))

    try:
        question = Question.objects.get(pk=pk)
        answers = question.answer_set.all()

        if request.method == 'POST':
            form = AnswerForm(user, question, request.POST)
            if form.is_valid():
                form.save()

                return redirect(reverse('question_page',kwargs={'pk': question.pk} ))
        else:
            form = AnswerForm(user, question)

        context = {
        'User': user,
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

    sessid = request.COOKIES.get('sessionid', None)
    if sessid:
        session = Session.objects.get(session_id=sessid)
        user = session.user

        if request.method == 'POST':
            form = AskForm(user, request.POST)
            if form.is_valid():
                try:
                    question = form.save()
                    url = question.get_absolute_url()
                    return HttpResponseRedirect(url)

                except:
                    form.add_error(None, 'Failed to create question')


        else:
            form = AskForm(user)


        context = {
            'form': form,
            'MainMenu': MainMenu,
            'SideMenu': SideMenu,
            'PageName': 'Add new question'
            }

    else:

        context = {}
    
    return render(request, 'add_question_template.html', context)