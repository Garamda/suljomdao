from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('signin/', signin, name="signin"),
    path('make/', make, name="make"),
    path('render/', now_make, name="now_make"),
    path('api/get_image/', get_image, name="get_image"),
    path('mypage/', mypage, name="mypage"),
]