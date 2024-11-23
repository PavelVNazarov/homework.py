from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # Показывать 5 постов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
