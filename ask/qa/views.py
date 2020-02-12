from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.core.paginator import Paginator
from .forms import AnswerForm, AskForm, MyLoginForm, MyRegisterForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class MyRegisterView(CreateView):
    model = User
    form_class = MyRegisterForm
    template_name = 'qa/register.html'
    success_url = reverse_lazy('main')
    success_msg = 'Success'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return form_valid


class MyLoginView(LoginView):
    template_name = 'qa/login.html'
    form_class = MyLoginForm
    success_url = reverse_lazy('main')

    def get_success_url(self):
        return self.success_url


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
        answer._user = request.user
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
        question = AskForm(request.POST) # type: AskForm
        question._user = request.user
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
