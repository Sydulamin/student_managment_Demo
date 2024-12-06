from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def login(request):
    if request.method == "POST":
       
        username = request.POST.get('uname')
        password = request.POST.get('pass1')

        if username and password:
            try:
                user = authenticate(username = username, password = password)
                
                if user:
                    print(user)
                    auth_login(request, user)
                    return redirect('home')
                else:
                    return redirect('login')
            except:
                return redirect('login')
        
        
    return render(request, 'auth/login.html')


def reg(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        number = request.POST.get('num')
        image = request.FILES.get('img')
        password = request.POST.get('pass1')
        password1 = request.POST.get('pass2')
        if len(password)>=8:
            if password == password1:
                user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username, email=email,
                                                phone_number=number, image=image, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, "Account Created.")
        else:
            messages.error(request, "Please Enter Atleast 8 Charecter Password.")
    return render(request, 'auth/registration.html')
