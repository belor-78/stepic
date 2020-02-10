from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.core.paginator import Paginator
from .forms import AnswerForm, AskForm


def test(request, *args, **kwargs):
    return HttpResponse('200 OK')


def new_questions(request):
    questions = Question.objects.new()
    page_num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    page = paginator.get_page(page_num)
    context = {'page': page}
    return render(request, 'qa/main.html', context=context)


def popular_questions(request):
    questions = Question.objects.popular()
    page_num = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)
    paginator = Paginator(questions, limit)
    page = paginator.get_page(page_num)
    context = {'page': page}
    return render(request, 'qa/main.html', context=context)


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/detail.html', context={'question': question, "answers": answers})


def to_answer(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        answer = AnswerForm(request.POST)
        if answer.is_valid():
            answer = answer.save(commit=False)
            answer.question = question
            return HttpResponseRedirect('/question/%d' % question.pk)
        else:
            context = {'form': answer}
            return render(request, 'qa/awswer.html', context)
    else:
        answer = AnswerForm()
        context = {'form': answer, 'question': question}
        print(context)
        return render(request, 'qa/answer.html', context)


def to_ask(request):
    if request.method == "POST":
        question = AskForm(request.POST)
        if question.is_valid():
            question = question.save()
            return HttpResponseRedirect('/question/%d' % question.pk)
        else:
            context = {'form': question}
            return render(request, 'qa/ask.html', context)
    else:
        question = AskForm()
        context = {'form': question}
        return render(request, 'qa/ask.html', context)
