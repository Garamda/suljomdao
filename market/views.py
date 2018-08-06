from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

def market_place(request):

    # 음료 종료 모두 보여주기
    context = {}


    return render(request, 'market/market.html', context)