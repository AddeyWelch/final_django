from django.shortcuts import render
from .models import Bounce

# Create your views here.


def home(request):
    return render(request, 'Rent/home.html')


def rental(request):
    # context to a variable Ex. {'Name': Name}
    bouncers = Bounce.objects.all()
    return render(request, 'Rent/rental.html', {'bouncers': bouncers})


def contact(request):
    return render(request, 'Rent/contact.html')

# def view_name(request, url, image, quantity, price, description):
#     all_bounces = Bounce.objects.all()
#     context = {'all_bounces': all_bounces}
#     context = {
#         'Quantity': 20,
#         'Prices': [100, 175],
#         'Description':
#     }
#     return render(request, 'rental.html', context)
