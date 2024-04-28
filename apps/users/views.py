from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


def auth(request):
    return render(request, 'users/auth.html', {})


def signup(request):
    if request.method == "GET":
        return render(request, "users/signup.html", {})
    elif request.method == "POST":
        user_informations = request.POST
        user_validation = User.objects.filter(username = user_informations['username']).first()
      
        if user_validation:
            return HttpResponse('Já existe um usuário com esse username.')
        
        user = User.objects.create_user(username=user_informations['username'], email=user_informations['email'], password=user_informations['password'])
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso')


def login(request):
    if request.method == "GET":
        return render(request, "users/login.html", {})
    elif request.method == "POST":
        user_informations = request.POST

        user = authenticate(username=user_informations['username'], password=user_informations['password'])
        
        if user:
            login_django(request, user)
            return HttpResponse('Autenticado.')
        else:
            return HttpResponse('Username ou senha inválidos.')
