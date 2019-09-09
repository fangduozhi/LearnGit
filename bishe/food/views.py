from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from food.models import food_daily
import math

def shouye(request):
    num = int(request.GET.get('nums', 1))
    foodlist=food_daily.objects.all()
    page_obj = Paginator(foodlist, 5)
    # 获取当前页数的数据
    try:
        per_page_list = page_obj.page(num)
    except PageNotAnInteger:
        per_page_list = page_obj.page(1)
    except EmptyPage:
        per_page_list = page_obj.page(page_obj.num_pages)
    # 每页开始码
    begin = (num - int(math.ceil(5)))
    if begin < 1:
        begin = 1
    # 每页结束码
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages
    else:
        begin = end - 9

    pagelist = range(begin, end + 1)
    return render(request,'caidan1.html',{'foodlist':per_page_list,'pagelist':pagelist,'currentNum':num})

def showfood_rc(request):
    foodlist= food_daily.objects.filter(ftype='food_rc')
    return render(request, 'food_rc.html', {'foodlist':foodlist})

def showfood_lc(request):
    foodlist=food_daily.objects.filter(ftype='food_lc')
    return render(request,'food_lc.html',{'foodlist':foodlist})

def showfood_tg(request):
    foodlist=food_daily.objects.filter(ftype='food_tg')
    return render(request,'food_tg.html',{'foodlist':foodlist})

def showfood_zs(request):
    foodlist=food_daily.objects.filter(ftype='food_zs')
    return render(request,'food_zs.html',{'foodlist':foodlist})

def showfood_xc(request):
    foodlist=food_daily.objects.filter(ftype='food_xc')
    return render(request,'food_xc.html',{'foodlist':foodlist})

def showfood_js(request):
    foodlist=food_daily.objects.filter(ftype='food_js')
    return render(request,'food_js.html',{'foodlist':foodlist})


def showfood_hx(request):
    foodlist=food_daily.objects.filter(ftype='food_hx')
    return render(request,'food_hx.html',{'foodlist':foodlist})

def indexshouye(request):
    return render(request,'shouye.html')

def showabout(request):
    return render(request,'about.html')