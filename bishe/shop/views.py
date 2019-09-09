from django.shortcuts import render
from login.views import *
from django.http import HttpResponse
from login.views import login
from .models import Goods

from food.models import food_daily
# Create your views here.

def addshop(request):
    sid=request.POST.get('sid')
    snum=request.POST.get('snum')
    uname=request.session.get('uname')
    pd=Goods.objects.filter(sid=sid).first()

    Goods.objects.create(sid=sid,count=snum,g_uname=uname)

    return render(request,'food_js.html')

def showshop(request):
    uname=request.session.get('uname')

    shopid=list(set(Goods.objects.filter(g_uname=uname).values_list('sid')))
    shop_list=[]
    for (i,) in shopid:

            goods=food_daily.objects.filter(fid=i).values_list('fname','price','gimg','fid')
            counts=Goods.objects.filter(sid=i).values_list('count')
            good ={
                'name':goods[0][0],
                'price':goods[0][1],
                'img':goods[0][2],
                'goodsid':goods[0][3],
                'getTotalPrice':int(goods[0][1])*int(counts[0][0]),
                'count':counts[0][0],
            }
            shop_list.append(good)

    return render(request, 'cart.html', {'cartItemList': shop_list})


