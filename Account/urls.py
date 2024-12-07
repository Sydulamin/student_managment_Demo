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
]
