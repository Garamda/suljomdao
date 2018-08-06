from django.urls import path
from .views import *

urlpatterns = [
    path('', market_place, name="market_place")
]