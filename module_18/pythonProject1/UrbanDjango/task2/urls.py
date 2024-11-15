from django.urls import path
from .views import ClassBasedView, func_based_view

urlpatterns = [
    path('class_view/', ClassBasedView.as_view(), name='class_view'),
    path('func_view/', func_based_view, name='func_view'),
]
