from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator

def test(request,*args,**kwargs):
    return HttpResponse('200 OK')

def new_questions(request):
    questions = Question.objects.new()
    page_num = request.GET.get('page',1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    page = paginator.get_page(page_num)
    context = {'page': page}
    return render(request, 'qa/main.html',context=context)

def popular_questions(request):
    questions = Question.objects.popular()
    page_num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    page = paginator.get_page(page_num)
    context = {'page': page}
    return render(request, 'qa/main.html', context=context)

def question_detail(request, pk):
    question = get_object_or_404(Question,pk=pk)
    answers = Answer.objects.filter(question=question)
    return render(request,'qa/detail.html',context={'question': question, "answers": answers})