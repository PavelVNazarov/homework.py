from django.shortcuts import render
from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(max_value=120, min_value=0)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']  # списком существующих пользователей
    info = {}

    if request.method == 'POST':
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
                return render(request, 'fifth_task/success.html', {'username': username})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    # Логика аналогична sign_up_by_django
    return sign_up_by_django(request)
