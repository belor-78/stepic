from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.core.paginator import Paginator
from .forms import AnswerForm, AskForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


class UserRegister(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'qa/register.html'


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


def detail_page(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'GET':
        form = AnswerForm({'question_id': question.pk})
    elif request.method == 'POST' and request.user.is_authenticated():
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return redirect('detail', pk=question.pk)
    return render(request, 'qa/detail.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form
    })


def to_answer(request, pk):
    question1 = Question.objects.get(pk=pk)
    if request.method == 'POST':
        answer = AnswerForm(request.POST)
        if answer.is_valid():
            # answer = answer.save(commit=False)
            # answer.question = question
            answer.save()
            return redirect('detail', pk=pk)
        else:
            context = {'form': answer, 'question': question1, 'answers': question1.answer_set.all()}
            return render(request, 'qa/answer.html', context)
    else:
        answer = AnswerForm({'question': question1.pk})
        context = {'form': answer, 'question': question1}
        # print(context)
        return render(request, 'qa/answer.html', context)


def to_ask(request):
    if request.method == "POST" and request.user.is_authenticated():
        question = AskForm(request.POST)  # type: AskForm
        if question.is_valid():
            question = question.save()
            return redirect(question.get_absolute_url())
        else:
            context = {'form': question}
            return render(request, 'qa/ask.html', context)
    else:
        question = AskForm()
        context = {'form': question}
        return render(request, 'qa/ask.html', context)
