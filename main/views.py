from django.http import Http404
from django.shortcuts import render
from main import models


def index(request):
    latest_articles = models.Article.objects.all().order_by("-createdAt")[:10]

    context = {
        'latest_articles': latest_articles
    }

    return render(request, 'main/index.html', context)


def article(request, pk):
    try:
        article = models.Article.objects.get(pk=pk)
    except:
        raise Http404()

    context = {
        "article": article
    }

    return render(request, 'main/article.html', context)


def author(request, pk):
    try:
        author = models.Author.objects.get(pk=pk)
    except:
        raise Http404()

    context = {
        'author': author
    }

    return render(request, 'main/author.html', context)


def create_article(request):
    context = {
        'authors': models.Author.objects.all()
    }

    if request.method == "POST":
        author = models.Author.objects.get(pk=request.POST['author'])

        article_data = {
            'title': request.POST['title'],
            'content': request.POST['content'],
            'author': author
        }

        models.Article.objects.create(**article_data)
        context["success"] = True

    return render(request, 'main/create_article.html', context)