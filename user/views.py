from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .models import User
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        
        exist_user = get_user_model().objects.filter(username=username)
        if exist_user:
            return render(request, 'signup.html')
        else:
            User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        guest = auth.authenticate(request, username=username, password=password)
        if guest is not None:
            auth.login(request, guest)
            return redirect('/home')
        else:
            return render(request, 'login.html')


def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home.html')
    else:
        return redirect('/login')