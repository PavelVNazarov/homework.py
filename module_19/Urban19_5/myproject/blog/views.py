from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all()
    post_count = int(request.GET.get('post_count', 5))  # По умолчанию 5
    paginator = Paginator(post_list, post_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'request': request})

