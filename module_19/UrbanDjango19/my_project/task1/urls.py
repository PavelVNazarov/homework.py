

from django.urls import path
from . import views
from .views import sign_up_by_django, sign_up_by_html, HomeView, StoreView, CartView

urlpatterns = [
    path('', HomeView.as_view(), name='main_page'),
    path('goods/', StoreView.as_view(), name='goods_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('register/', sign_up_by_django, name='sign_up'),
    path('django_sign_up/', sign_up_by_html, name='django_sign_up'),
    path('games/', StoreView.as_view(), name='games_list'),
]