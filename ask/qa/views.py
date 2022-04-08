from django.http import HttpResponse, Http404
from django.shortcuts import render
from qa.models import Question
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def new_questions(request):


    question_list = Question.objects.new()
    paginator = Paginator(question_list, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'q_list': page_obj}

    return render(request, 'new_question_template.html', context)


def pop_questions(request):

    question_list = Question.objects.popular()
    paginator = Paginator(question_list, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {'q_list': page_obj}

    return render(request, 'pop_question_template.html', context)


def question_page(request, pk):

    try:
        question = Question.objects.get(pk=pk)
        answers = question.answer_set.all()

        context = {
        'question': question,
        'answers': answers,
        }

    except Question.DoesNotExist:
        raise Http404

    return render(request, 'question_page_template.html', context)