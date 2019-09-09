from django.shortcuts import render
from json import loads
from .models import Order
import time
from shop.models import Goods
from food.models import food_daily
# Create your views here.
def show_order(request):
    goods = request.GET.get('goods')
    uname = request.session.get('uname')
    print(goods)
    num=0
    sum = 0
    button_list=[]
    orderid=get_order_code()
    if goods !='' and goods is not None:
        button_list=loads('['+goods[:-1]+']')
        for b in button_list:
            num = b['num']
            price = b['price']
            s_price = b['s_price']
            gname = b['gname']
            img=b['img']
            sum += int(b['s_price'][1:])
            Order.objects.create(u_name=uname,o_img=img,orderid=orderid,oshopname=gname,oprice=price,ocount=num,oammount=s_price)
            foodname=food_daily.objects.filter(fname=gname).values_list('fid')
            for (i,) in foodname:
                Goods.objects.filter(sid=i).delete()

    return render(request, 'dingdan.html',{'goods':button_list,'sum':sum})



def in_order(request):
        uname=request.session.get('uname')
        goods =request.GET.get('goods')
        button_list = []
        return render(request,'jiesuan.html')


def get_order_code():
        order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
        return order_no

def myorder(request):
    uname=request.session.get('uname')
    orderid=list(set(Order.objects.filter(u_name=uname).values_list('orderid')))
    orderlist=[]
    orderids=[]
    for (i,) in orderid:
        orders=Order.objects.filter(orderid=i)
        orderlist.append(orders)
        orderids.append(i)
    print(orderids)
    print(orderlist)
    return render(request,'user_order.html',{'orderlist':orderlist,'orderid':i})


def orderwwc(request):
    uname=request.session.get('uname')
    orderid=list(set(Order.objects.filter(u_name=uname,state='未完成').values_list('orderid')))
    orderwwc=Order.objects.filter(state='未完成')

    orderlist = []
    if orderid:
        for (i,) in orderid:
            orders = Order.objects.filter(orderid=i)
            if orders:
                orderlist.append(orders)
        return render(request,'orderwwc.html',{'orderlist':orderlist,'orderid':i})
    return render(request,'orderwwc.html')

def orderywc(request):
    uname = request.session.get('uname')
    orderid = list(set(Order.objects.filter(u_name=uname, state='已完成').values_list('orderid')))
    orderywc = Order.objects.filter(state='已完成')
    orderlist = []
    if orderid:
        for (i,) in orderid:
            orders = Order.objects.filter(orderid=i)
            if orders:
                orderlist.append(orders)
        return render(request, 'orderywc.html', {'orderlist': orderlist,'orderid':i})
    return render(request,'orderywc.html')