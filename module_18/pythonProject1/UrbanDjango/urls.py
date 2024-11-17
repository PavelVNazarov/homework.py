from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/', include('task2.urls')),  # Подключаем маршруты task2
    #path('task3/', include('task3.urls')),  # Подключаем маршруты task3
    path('task4/', include('task4.urls')),
    path('task5/', include('task5.urls')),
]
# from django.urls import path
# from task5.views import sign_up_by_django, sign_up_by_html
#
# urlpatterns = [
#     path('', sign_up_by_django, name='sign_up'),
#     path('django_sign_up/', sign_up_by_html, name='sign_up_django'),
# ]
