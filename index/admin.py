from django.contrib import admin
from .models import *
# Register your models here.
class FinBoard(admin.ModelAdmin):
    list_display = ('user', 'ingredient', 'css', 'is_st','is_ice','bg_color','specials_name')

admin.site.register(request_make)
admin.site.register(special)
admin.site.register(make_sul,FinBoard)
admin.site.register(cat_text)
admin.site.register(cat_fin_text)
admin.site.register(fin_sul_text)