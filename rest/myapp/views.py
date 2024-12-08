from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

def contact(request):
    return render(request,'contact.html')

def admin(request):
    return render(request,'admin.html')
