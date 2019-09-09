
from django.urls import path
from . import views
urlpatterns = [
    path('showshop/', views.showshop, name='gwc'),
    path('addshop/',views.addshop)
]