from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q
import random
from datetime import datetime


def home(request):
    return render(request, 'index.html')


def articles(request, string=None):
    author = string.replace('%20', ' ') if string and '%20' in string else string
    if author:
        post = Post.objects.filter(post_author=author).order_by('-post_date')
    else:
        post = Post.objects.filter(is_post_approved=True).order_by('-post_date')
    paginator = Paginator(post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles.html', {'post': page_obj, 'author': author})


def blog_post(request, pk=None):
    post = Post.objects.get(id=pk)
    post_suggestion = list(Post.objects.filter(~Q(id=post.pk), Q(is_post_approved=True))[:6])
    post_authors = list(Post.objects.filter(is_post_approved=True).distinct('post_author')[:6])
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


def write_for_us(request):
    if request.method == 'POST':
        post = Post()
        if not Post.objects.filter(post_title=request.POST.get('post_title')):
            if request.FILES.get('post_image'):
                post.post_image = request.FILES['post_image']
            post.post_author = request.POST.get('post_author')
            post.post_title = request.POST.get('post_title')
            post.post_content = request.POST.get('post_content')
            post.post_date = datetime.now()
            post.save()
            return render(request, 'thanks_for_submitting.html')
    return render(request, 'write_for_us.html')


def page_not_found_view(request, exception):
    return render(request, '404.html')
