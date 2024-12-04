from django.shortcuts import render
from .models import CustomUser


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def login(request):
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

        if password == password1:
            user = CustomUser.objects.create(first_name=first_name, last_name=last_name, username=username, email=email,
                                             phone_number=number, image=image, password=password)
            user.set_password(password)
            user.save()
    return render(request, 'auth/registration.html')
