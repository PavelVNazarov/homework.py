from django.shortcuts import render, redirect

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        'item1': 'Игра A - 1000 руб.',
        'item2': 'Игра B - 1500 руб.',
        'item3': 'Игра C - 2000 руб.',
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')