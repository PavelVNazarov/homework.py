from django.shortcuts import render

def main_page(request):
    return render(request, 'third_task/platform.html')

def shop_page(request):
    items = {
        "item1": "Игра 1",
        "item2": "Игра 2",
        "item3": "Игра 3"
    }
    return render(request, 'third_task/games.html', {'items': items})

def cart_page(request):
    return render(request, 'third_task/cart.html')
