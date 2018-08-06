from django.db import models
from django.contrib.auth.models import User
from market.models import market_img

# Create your models here.
class request_make(models.Model):
    text = models.CharField(max_length=250, verbose_name="요청사항")

    def __str__(self):
        return self.text


class cat_text(models.Model):
    text = models.CharField(max_length=250, verbose_name="고양이 대사")
    def __str__(self):
        return self.text

class cat_fin_text(models.Model):
    text = models.CharField(max_length=250, verbose_name="고양이 대사")

    def __str__(self):
        return self.text

class special(models.Model):
    text = models.CharField(max_length=250, verbose_name="특수 능력치")

    def __str__(self):
        return self.text

class fin_sul_text(models.Model):
    text = models.CharField(max_length=250, verbose_name="마지막 술 설명")

    def __str__(self):
        return self.text

# 술잔에 따라 각 코드가 세부적으로 변함.
class make_sul(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    sul_jan = models.CharField(max_length=250, verbose_name="술잔 모양, st 존재시, 세모모양 제외")
    sul_name = models.CharField(max_length=250, verbose_name="술이름", default="폭풍의 ")
    ingredient = models.CharField(max_length=250, verbose_name="재료들 id")
    gradient = models.BooleanField(default=False, verbose_name="음료색 그라디언트")
    css = models.CharField(max_length=250, verbose_name="음료 색상, css 코드")

    is_st = models.BooleanField(default=False, verbose_name="건더기 유무")
    st1 = models.CharField(max_length=250, verbose_name="건더기1", default="none")
    st2 = models.CharField(max_length=250, verbose_name="건더기2", default="none")

    is_ice = models.BooleanField(default=False, verbose_name="아이스크림 유무")
    ice = models.CharField(max_length=250, verbose_name="아이스크림 코드")

    bg_color = models.CharField(max_length=100, verbose_name="음료 배경색")


    desc =models.CharField(max_length=250, verbose_name="설명 랜덤", default="스윙스 땀 맛이나는 음료가 생성되었다!")

    headache = models.CharField(max_length=250, verbose_name="숙취도 수치", default="%")
    degreeOfPig = models.CharField(max_length=250, verbose_name="비만도 수치", default="Kcal")
    specials_name = models.CharField(max_length=250, verbose_name="특수 능력치")
    specials = models.CharField(max_length=250, verbose_name="특수 능력치 수치")

