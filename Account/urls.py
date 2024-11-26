from django.urls import path
from .views import home,login,reg

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('reg/', reg, name='reg'),
]
