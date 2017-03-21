from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Rent/home.html')


def rental(request):
    return render(request, 'Rent/rental.html')


def contact(request):
    return render(request, 'Rent/contact.html')
