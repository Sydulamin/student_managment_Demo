from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('reg/', reg, name='reg'),
    path('get-counter/', get_counter, name='get_counter'),
    path('increment-counter/', increment_counter, name='increment_counter'),
    path('decrement-counter/', decrement_counter, name='decrement_counter'),
    path('page/', page, name='page'),
    path('otp_verify/', otp_verify, name='otp_verify'),
<<<<<<< HEAD
    path('logout_user/', logout_user, name='logout_user'),
=======
>>>>>>> 5b4fadeb83ccad2dcf8c139071b63e812db12624
]
