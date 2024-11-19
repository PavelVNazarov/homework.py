from django.views import View
from django.shortcuts import render
from .forms import UserRegister

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


# Псевдо-список существующих пользователей
users = ["user1", "user2", "user3"]

def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/registration_page.html', {"info": info, "success": f"Приветствуем, {username}!"})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    # Можно реализовать аналогично первому представлению
    return sign_up_by_django(request)