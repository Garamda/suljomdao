from django.contrib import admin
from .models import *

class FinBoard(admin.ModelAdmin):
    list_display = ('id','name', 'types','description', 'img_index', 'imgs','bg_color')
admin.site.register(market_img,FinBoard)
