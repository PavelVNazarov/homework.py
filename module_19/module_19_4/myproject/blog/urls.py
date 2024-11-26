from django.urls import path
from .views import post_list
from .views import update_post, get_all_posts, delete_post, filter_posts

urlpatterns = [
    path('update_post/', update_post, name='update_post'),
    path('get_all_posts/', get_all_posts, name='get_all_posts'),
    path('delete_post/', delete_post, name='delete_post'),
    path('filter_posts/', filter_posts, name='filter_posts'),
    path('', post_list, name='post_list'),
]