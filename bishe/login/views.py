from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from utils.code import *
import re
# Create your views here.
def zhuce (request):
    return render(request,'register.html')
def addUser(request):
    uname=request.POST.get('uname')
    upassword=request.POST.get('upassword')
    repassword=request.POST.get('repassword')
    uphone=request.POST.get('uphone')


    if upassword==repassword and checkphone(uphone)!=None  :
        registAdd=User.objects.create(uname=uname,upassword=upassword,uphone=uphone)
        message='注册成功！'
    if upassword!=repassword:
        message='两次输入密码不同！'
        return render(request,'register.html',{'message':message})
    if checkphone(uphone)==None:
        mport='输入手机号号码不符合规范'
        return render(request,'register.html',{'message':message})
    return render(request,'register.html',{'message':message})
def login(request):
    if request.method=='POST':
        uid=request.POST.get('uid')
        uname=request.POST.get('uname')
        upassword=request.POST.get('upassword')
        uyzm=request.session.get('yzm')
        request.session['uname'] = uname
        ucode=request.POST.get('ucode')


        if uname and upassword and uyzm==ucode:
            try:
                user=User.objects.get(uname=uname)

                if user.upassword==upassword:


                    return render(request,'caidan1.html')


                else:
                    message='密码不正确！'
            except:
                message='用户名不存在！'
            return render(request,'index.html',{'message':message})
    return render(request,'index.html')
def checkphone(uphone):
    pat = r"^1(([35789]\d)|(47))\d{8}$"
    res = re.match(pat, uphone)
    return res

def getCode(request):
    img,txt=gene_code()

    request.session['yzm']=txt

    return HttpResponse(img,content_type='image/png')


def checkCode(request):
    code=request.GET.get('code')

    sessioncode=request.session.get('yzm')

    flag = code == sessioncode

    return HttpResponse(flag)


def checkuname(request):
    uname=request.GET.get('uname')

    uup=str(User.objects.filter(uname=uname).first())

    return HttpResponse(uup)



