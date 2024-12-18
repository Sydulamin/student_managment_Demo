from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CustomUser, Counter
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
import random
from django.conf import settings


def home(request):
    return render(request, 'home/home.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass1')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_verified:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Please verify your account.")
                    return redirect('otp_verify')
            else:
                messages.error(request, "Invalid username or password.")
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

        if len(password) < 8:
            messages.error(request, "Please enter at least an 8 character password.")
        elif password != password1:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                otp = random.randint(0000, 9999)
                user = CustomUser(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    phone_number=number,
                    image=image,
                    otp=otp
                )
                user.set_password(password)
                user.save()

                send_mail(
                    "Your Account verification OTP",
                    f"Here is Your otp : {otp}.",
                    settings.EMAIL_HOST_USER,
                    [email],
                )

                messages.success(request, "Check your email inbox for the verification otp.")
                return redirect('otp_verify')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('reg')

    return render(request, 'auth/registration.html')


def otp_verify(request):
    if request.method == 'GET':
        otp = request.GET.get('otp')
        if otp:
            user = CustomUser.objects.get(otp=otp)
            if user:
                user.is_verified = True
                user.save()
                return redirect('login')
            else:
                messages.error(request, "Wrong verification otp.")
                return redirect('otp_verify')
    return render(request, 'auth/otp.html')


def page(request):
    return render(request, 'counter.html')


def get_counter(request):
    counter = Counter.objects.get(id=1)
    return JsonResponse({'value': counter.value})


def increment_counter(request):
    counter = Counter.objects.get(id=1)
    counter.value += 1
    counter.save()
    return JsonResponse({'value': counter.value})


def decrement_counter(request):
    counter = Counter.objects.get(id=1)
    counter.value -= 1
    counter.save()
    return JsonResponse({'value': counter.value})
