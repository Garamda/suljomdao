from django.db import models

# Create your models here.
class Ingredients(models.Model):
    barcode = models.CharField(max_length=250, verbose_name="재료 별 HASH 값")
    name = models.CharField(max_length=30, verbose_name="술 이름")
    gens = models.IntegerField(verbose_name="Gens")
    price = models.CharField(max_length=100, verbose_name="ETH 가격")
    created = models.DateTimeField(verbose_name="생성 시간")
    imgs = models.ImageField(upload_to='ing/', verbose_name="재료 이미지")

    def __str__(self):
        return self.name

class market_img(models.Model):
    name = models.CharField(max_length=250, verbose_name="술 이름(영어)")
    description = models.CharField(max_length=250, default='맛있는술', verbose_name="술 설명")
    types = models.CharField(max_length=200, default='alcohol', verbose_name='필터 타입')
    img_index = models.CharField(max_length=255, default=0, verbose_name="이미지 인덱스 번호")
    imgs = models.ImageField(upload_to='image/', verbose_name="이미지 파일")
    bg_color = models.CharField(max_length=200, verbose_name="배경색", default="#")
    def __str__(self):
        return self.name
