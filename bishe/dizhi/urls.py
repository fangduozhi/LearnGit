from django.urls import path
from . import views
urlpatterns = [
    path('address/',views.show_address)
]