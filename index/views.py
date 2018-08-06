from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from market.models import market_img
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import random
from django.db.models import Q
import json

def index(request):
    logout(request)
    return render(request, 'index/index.html')


def signin(request):
    if request.method == "POST":

        # validate
        wallet = request.POST.get('eth_wallet')
        if wallet == "":
            return redirect("/")
        is_user = User.objects.filter(username=wallet)

        # signup
        if len(is_user) == 0:
            users = User.objects.create(
                username=wallet,
                last_name=1
            )
            request.session["address"] = users.username
            request.session["level"] = users.last_name

            login(request, users)
            return redirect('market_place')

        # signin
        elif len(is_user) == 1:

            request.session["address"] = is_user[0].username
            request.session["level"] = is_user[0].last_name

            login(request, is_user[0])

            return redirect('market_place')
        else:
            logout(request)
            return redirect('/')

    else:
        logout(request)
        return redirect('/')


def get_image(request):
    if request.is_ajax():
        name = request.POST.get('tokenName')

        print(name)
        try:
            obj = market_img.objects.get(name=name)
            mkImg = obj.imgs.url
            des = obj.description
            types = obj.types
            id = obj.id
            return JsonResponse({"img": mkImg, "des":des, "types":types, "id":id})
        except:
            mkImg = ''
            des = ''
            types = ''
            id = ''
            return JsonResponse({"img": mkImg, "des": des, "types":types})

@login_required(login_url='/')
def make(request):
    context = {}
    context["request_make"] = request_make.objects.all()

    is_user = User.objects.filter(username=request.session["address"])[0]
    context["level"] = is_user.last_name

    if int(is_user.last_name) <= 5:
        context["make_range"] = range(0,2)
    elif 5 < int(is_user.last_name) <= 15:
        context["make_range"] = range(0,3)
    elif 15< int(is_user.last_name) <= 20:
        context["make_range"] = range(0,4)
    elif 20 <  int(is_user.last_name):
        context["make_range"] = range(0,5)

    return render(request, 'make.html', context)


# url: render/
@login_required(login_url='/')
def now_make(request):
    context = {}
    is_user = User.objects.filter(username=request.session["address"])[0]
    context["level"] = is_user.last_name
    if request.method == "POST":
        context["request_make"]=request_make.objects.get(id=request.POST.get('req_make')).text

        context["tkid"] = request.POST.get('tkid')

        context["cat_text"] = random.choice(cat_text.objects.all())
        context["fin_text"] = random.choice(cat_fin_text.objects.all())
        asset_data = request.POST.get('tkid').split(",")

        # 여기서 찍어내야함.
        context["cat_text"] = random.choice(cat_text.objects.all())
        bg_set = [ "#9DE04F" "#6E0E10", "#FFE528", '#FF653A', "#C3D1D3","#00E2BC","#F9BD50","#0063FF",'#E20800','#646464','#B10ACF',"#FFE6D9","#FF03A7","#FF3B3B","#91CAFF"]
        context["bg_color"] = random.choice(bg_set)


        array_st = []
        array_ice = []

        st_counter = 0
        ice_counter = 0

        drink_bg = []
        bg_counter = 0

        # 일반, 둥근, 삼각
        sul_jan_code = [0, 1, 2]
        q_asset = []
        for each in asset_data:
            ingre = market_img.objects.get(id=each)
            q_asset.append(ingre.id)
            print(ingre.id)
            # 건더기 유무
            if ingre.types == "something":
                array_st.append(ingre)
                st_counter += 1
                try:
                    sul_jan_code.pop(2)
                except:
                    pass

            # 아이스크림 유무
            if ingre.types == "icecream":
                array_ice.append(ingre)
                ice_counter += 1

            # 음료
            if ingre.types == "drink" or ingre.types == "alcohol":
                drink_bg.append(ingre.bg_color)
                bg_counter += 1

        context["suljan"] = random.choice(sul_jan_code)
        # random gra color choice
        gra_counter = 0
        gra_color = []

        # 2개 이상 / 랜덤 확률 / 짝수id
        checker = len(drink_bg) >= 2 and random.choice(range(1, 3)) < (bg_counter * 2)
        print(checker)
        if checker:
            gra_counter += random.choice(range(2, bg_counter + 1))

            for each in range(0, gra_counter):
                selec = random.choice(drink_bg)
                gra_color.append(selec)
                drink_bg.pop(drink_bg.index(selec))

            base_color = ""
            for i in gra_color:
                base_color += (i + ",")

            base_color = base_color[:-1]

            is_gra = "Y"
        else:
            # 랜덤 bg / 홀수 id
            base_color = random.choice(drink_bg)
            is_gra = "N"

        context["base"] = base_color
        context["is_gra"] = is_gra

        # 건더기 랜덤 or 3개까지....
        if st_counter >= 1:
            if st_counter == 5:
                array_st.pop(random.choice(range(0, 4)))
                array_st.pop(random.choice(range(0, 3)))
                re_st = array_st
            elif st_counter == 4:
                array_st.pop(random.choice(range(0, 3)))
                re_st = array_st
            else:
                re_st = array_st
        else:
            re_st = []

        context["st"] = re_st

        # 아이스크림
        if ice_counter >= 1:
            re_ice = random.choice(array_ice)

        else:
            re_ice = ''

        context["ice"] = re_ice

        # DB 등록
        if is_gra == "Y":
            gradient = True
        else:
            gradient = False
        if len(context["st"]) > 1:
            db_st = True
        else:
            db_st = False
        id_st = []
        for each in context["st"]:
            id_st.append(each.id)

        if context["ice"]:
            db_ice = True
        else:
            db_ice = False

        try:
            ice_id = context["ice"]
        except:
            ice_id = ''

        sul_name_set = ["최강의 ", "폭풍의 ", "존맛탱 ", "부랑자의 ", "천둥의 ", "주작의 "]

        regi_sul = make_sul.objects.create(
            user=User.objects.get(username=request.session["address"]),
            sul_jan = context["suljan"],
            gradient= gradient,
            css = context["base"],
            ingredient = q_asset,
            is_st = db_st,
            st1 = id_st,
            desc= random.choice(fin_sul_text.objects.all()).text,
            is_ice = db_ice,
            ice = ice_id,
            sul_name=random.choice(sul_name_set),
            bg_color = context["bg_color"],
            headache = str( random.choice(range(1,101)) ),
            degreeOfPig = str( random.choice(range(0,100000000)) ),
            specials_name = random.choice(special.objects.all()).text,
            specials = str( random.choice(range(0,1000)) )
        )

        return render(request, 'rendering/rendering.html', context)
    else:
        return redirect('/')

@login_required(login_url='/')
def mypage(request):
    context = {}
    is_user = User.objects.filter(username=request.session["address"])[0]
    context["level"] = is_user.last_name
    my_sets = make_sul.objects.filter(user=User.objects.get(username=request.session["address"]))
    context["my"] = []
    for each in my_sets:

        # 재료 정보
        ingredient = []
        for id in json.loads(each.ingredient):
            ingredient.append(market_img.objects.get(id=id))

        if len(ingredient) > 3:
            ingre1 = ingredient[:3]
            ingre2 = ingredient[3:]
        else:
            ingre1 = ingredient
            ingre2 = ""

        st = []
        for ss in json.loads(each.st1):
            st.append(market_img.objects.get(id=ss))

        try:
            ice = market_img.objects.get(id=each.ice)
        except:
            ice = ""

        if each.gradient:
            is_gra="Y"
        else:
            is_gra = "N"



        context["my"].append({
            "index":each.id,
            "name":each.sul_name + each.specials_name +" 술",
            "suljan": int(each.sul_jan),
            "counter_ingre":len(ingredient),
            "ingredient":ingredient,
            "ingre1":ingre1,
            "ingre2":ingre2,
            "css":each.css,
            "st":st,
            "ice":ice,
            "bg":each.bg_color,
            "desc":each.desc,
            "headache":each.headache,
            "degreeOfPig":each.degreeOfPig,
            "specials_name":each.specials_name,
            "specials":each.specials,

            "is_gra":is_gra


        })


    return render(request, 'mypage.html', context)