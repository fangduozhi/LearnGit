from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('showorder/',views.show_order,name='order' ),
    path('inorder/',views.in_order,name='inorder'),
    path('myorder/',views.myorder),
    path('orderwwc/',views.orderwwc),
    path('orderywc/',views.orderywc)
]