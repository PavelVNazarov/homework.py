# для заполнения базы данных условными постами разных авторов
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from blog.models import Post

for i in range(1, 13):
    Post.objects.create(title=f'Пост {i}', content=f'Содержимое поста {i}', author=f'Автор {str(i)}', pub_date=f'Дата {i}')