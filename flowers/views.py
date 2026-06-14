from django.shortcuts import render

def home(request):
    return render(request, 'flowers/home.html')

def collections(request):
    return render(request, 'flowers/collections.html')

def services(request):
    return render(request, 'flowers/services.html')

def about(request):
    return render(request, 'flowers/about.html')

def contact(request):
    return render(request, 'flowers/contact.html')

def order(request):
    return render(request, 'flowers/order.html')

def dashboard(request):
    return render(request, 'flowers/dashboard.html')
