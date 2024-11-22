from django.views import View
from django.shortcuts import render
from .forms import UserRegister
from .models import Game, Buyer

class HomeView(View):
    def get(self, request):
        return render(request, 'fourth_task/platform.html')

class StoreView(View):
    def get(self, request):
        context = {'games': ['Atomic Heart', 'Cyberpunk 2077']}
        return render(request, "fourth_task/games.html", context)

class CartView(View):
    def get(self, request):
        return render(request, "fourth_task/cart.html")

# Псевдо-список существующих пользователей
users = ["user1", "user2", "user3"]

def handle_sign_up(form, info):
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
            return True, username
    return False, None

def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        success, username = handle_sign_up(form, info)
        if success:
            return render(request, 'fifth_task/registration_page.html', {"info": info, "success": f"Приветствуем, {username}!"})
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    return sign_up_by_django(request)


def home(request):
    return render(request, 'task1/home.html')

def product_list(request):
    games = Game.objects.all()
    return render(request, 'task1/product_list.html', {'games': games})

def cart(request):
    return render(request, 'task1/cart.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        if not Buyer.objects.filter(name=name).exists():
            buyer = Buyer.objects.create(name=name, balance=0, age=18)  # Возраст можно изменить
            buyer.save()
    return render(request, 'task1/register.html')