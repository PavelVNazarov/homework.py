from django.contrib import admin
from .models import Post

@admin.register(Post)  # Использование декоратора для регистрации модели
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')  # Поля, отображаемые в списке
    search_fields = ('title', 'content',)  # Поиск по заголовку и содержимому