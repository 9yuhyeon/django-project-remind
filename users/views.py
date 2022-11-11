from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login as loginsession

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')

        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return redirect(request, 'users:login')
        else:
            return HttpResponse('틀렸다 비밀번호가')
    else:
        return HttpResponse('허용되지 않는 메소드 / 좋지 않은 코드')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('community:index')
        else:
            return HttpResponse('로그인 실패!')

# 필요없는 놈
def user(request):
    return HttpResponse(request.user)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user':user,
    }
    return render(request, 'profile.html', context)