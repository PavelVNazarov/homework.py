from task4.views import view1, view2

urlpatterns = [
    path('view1/', view1, name='view1'),
    path('view2/', view2, name='view2'),
]