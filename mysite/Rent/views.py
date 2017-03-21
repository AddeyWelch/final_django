from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'rent/home.html')


def rental(request):
    return render(request, 'rent/rental.html')


def contact(request):
    return render(request, 'rent/contact.html')
