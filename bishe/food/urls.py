from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('caidan/',views.shouye,name='zy'),
    path('login/caidan/caidan_rc/',views.showfood_rc,name='rc'),
    path('login/caidan/caidan_lc/',views.showfood_lc,name='lc'),
    path('login/caidan/caidan_tg/',views.showfood_tg,name='tg'),
    path('login/caidan/caidan_zs/',views.showfood_zs,name='zs'),
    path('login/caidan/caidan_xc/',views.showfood_xc,name='xc'),
    path('login/caidan/caidan_js/',views.showfood_js,name='js'),
    path('login/caidan/caidan_hx/',views.showfood_hx,name='hx'),
    path('',views.indexshouye,name='sy'),
    path('about/',views.showabout,name='about'),

]
