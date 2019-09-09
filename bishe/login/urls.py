
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.zhuce,name='zc'),
    path('addUser/',views.addUser),
    path('login/',views.login,name='lg'),
    path('Code/',views.getCode),
    path('checkCode/',views.checkCode),
    path('checkuname/',views.checkuname),
]