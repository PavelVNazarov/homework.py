
from django.urls import path
from . import views
from django.urls import path
from .views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('', views.HomeView, name='main_page'),  # Главная страница
    path('goods/', views.StoreView, name='goods_list'), # Список товаров
    path('cart/', views.CartView, name='cart'), # Корзина
    # path('register/', views.register, name='register'), # Регистрация
    path('register/', sign_up_by_django, name='sign_up'),
    path('django_sign_up/', sign_up_by_html, name='django_sign_up'),
]