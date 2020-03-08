from django.shortcuts import render, get_object_or_404

from .models import Article
from taggit.models import Tag

def home(request):

    posts = Article.objects.all()

    return render(request, 'home.html', {'posts': posts})

def fortag(request, slug):

    tag = get_object_or_404(Tag, slug = slug)

    posts = Article.object.filter(Tag = tag)

    context = {
        'tag' : tag,
        'posts' : posts
    }

    return render(request, 'fortag.html', context)


def post(request, pk):

    Post = get_object_or_404(Article, pk=pk)

    return render(request, 'post.html', {'Post': Post})


def sobre(request):

    return render(request, 'sobre.html')