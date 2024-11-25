from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all()
    post_count_str = request.GET.get('post_count', '5')  # По умолчанию 5

    # Проверка на пустое значение
    if post_count_str:
        try:
            post_count = int(post_count_str)
        except (ValueError, TypeError):
            post_count = 5  # Оставляем значение по умолчанию
    else:
        post_count = 5  # Оставляем значение по умолчанию
    paginator = Paginator(post_list, post_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'request': request})