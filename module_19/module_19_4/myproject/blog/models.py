from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Поле для заголовка
    content = models.TextField()               # Поле для содержимого
    author = models.CharField(max_length=100)  # Поле для автора
    pub_date = models.DateTimeField(auto_now_add=True)  # Дата публикации

    def __str__(self):
        return self.title  # Возвращает заголовок поста при вызове объекта
