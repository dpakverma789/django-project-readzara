from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q
import random


def home(request):
    return render(request, 'index.html')


def articles(request, string=None):
    if string:
        post = Post.objects.filter(post_author=string).order_by('-post_date')
    else:
        post = Post.objects.all().order_by('-post_date')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles.html', {'post': page_obj, 'author': string})


def blog_post(request, pk=None):
    post = Post.objects.get(id=pk)
    post_suggestion = list(Post.objects.filter(~Q(id=post.pk))[:6])
    post_authors = list(Post.objects.all().distinct('post_author')[:6])
    random.shuffle(post_suggestion)
    random.shuffle(post_authors)
    if post:
        data = {
            'post_image': post.post_image,
            'post_title': post.post_title,
            'post_content': post.post_content,
            'post_author': post.post_author,
            'post_date': post.post_date
        }
        context = {'data': data, 'post_suggestion': post_suggestion, 'post_authors': post_authors}
        return render(request, 'post.html', context)


def about(request):
    return render(request, 'about.html')


def page_not_found_view(request, exception):
    return render(request, '404.html')
