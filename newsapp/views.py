from django.shortcuts import render
from newsapp.models import News


def index(request):
    context = {'news_list': News.objects.all()}
    return render(request, 'index.html', context)


def create_news(request):
    context = {}

    if request.POST:
        title = request.POST.get('title')
        text = request.POST.get('text')
        new_news = News(title=title, text=text, short_text=text[:255])
        new_news.save()

    return render(request, 'create-news.html', context)
