from django.shortcuts import render

# Create your views here.
def show_address(request):

    return render(request,'user_address.html')