from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from newsapp.models import News
from newsapp.form import RegistrationForm, SettingsForm


@login_required
def index(request):
    context = {'news_list': News.objects.filter(topic__in=request.user.topic_set.all()).all()}
    return render(request, 'index.html', context)


@login_required
def create_news(request):
    context = {}

    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        new_news = News(title=title, text=text, short_text=text[:255])
        new_news.save()

    return render(request, 'create-news.html', context)


def log_in(request):
    if request.POST.get('username') and request.POST.get('password'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/news/')

    return render(request, 'user-login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(password=form.cleaned_data['password1'], username=form.cleaned_data['username'])
            new_user.save()
            login(request, new_user)
            return redirect('/news/')
    else:
        form = RegistrationForm()

    return render(request, 'user-register.html', {'form': form})


@login_required
def settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            for topic in form.cleaned_data['topics']:
                request.user.topic_set.add(topic)
            return redirect('/news/')
    else:
        form = SettingsForm()
    return render(request, 'settings.html', {'form': form})
