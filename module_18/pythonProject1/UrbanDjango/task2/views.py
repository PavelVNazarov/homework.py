from django.shortcuts import render
from django.views import View

class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')

def func_based_view(request):
    return render(request, 'second_task/func_template.html')
