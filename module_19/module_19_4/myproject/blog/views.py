from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.all()

    # Получаем количество постов на странице из параметра запроса, или по умолчанию 5
    posts_per_page = request.GET.get('posts_per_page', 5)

    paginator = Paginator(posts, posts_per_page)  # Показывать заданное количество постов
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def update_post(request):
    # Изменение заголовка поста с id = 1
    post = Post.objects.get(id=1)  # Получаем пост с id = 1
    post.title = 'Новый заголовок'
    post.save()  # Сохраняем изменения
    return HttpResponse('Пост обновлён!')

def get_all_posts(request):
    # Запрос на получение всех объектов и их вывод
    all_posts = Post.objects.all()  # Получение всех постов
    titles = "<br>".join([post.title for post in all_posts])  # Формируем строку заголовков
    return HttpResponse(f'Все посты:<br>{titles}')

def delete_post(request):
    # Удаление одного из объектов
    post_to_delete = Post.objects.get(id=1)  # Получаем пост с id = 1
    post_to_delete.delete()  # Удаляем пост
    return HttpResponse('Пост удалён!')

def filter_posts(request):
    # Фильтрация объектов в базе данных
    filtered_posts = Post.objects.filter(pub_date__year=2024)  # статьи опубликованные в 2024 году
    titles = "<br>".join([post.title for post in filtered_posts])  # Формируем строку заголовков
    return HttpResponse(f'Фильтрованные посты:<br>{titles}')