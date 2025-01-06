from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .tools import valid_user


users = ['Kate', 'Jon', 'Tim', 'Urban']

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        error = valid_user(username, password, repeat_password, age, users)
        if error:
            info['error'] = error
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            error = valid_user(username, password, repeat_password, age, users)
            if error:
                form.add_error(None, error)
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)


