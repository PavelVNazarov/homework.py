from django.views import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request):
        return render(request, "fourth_task/platform.html")

class StoreView(View):
    def get(self, request):
        context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
        return render(request, "fourth_task/games.html", context)

class CartView(View):
    def get(self, request):
        return render(request, "fourth_task/cart.html")