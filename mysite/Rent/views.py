from django.shortcuts import render, redirect
from .models import Bounce
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'Rent/home.html')


def contact(request):
    return render(request, 'Rent/contact.html')


def view_form(request):
    if request.method == 'GET':
        bouncers = Bounce.objects.all()
        # form = BounceIntoFun()
        return render(request, 'Rent/rental.html', {'bouncers': bouncers})
    else:
        # form = BounceIntoFun(request.POST)
        # print(form)
        return redirect('mysite:rental')


def rent(request, item_id):
    item = Bounce.objects.get(pk=item_id)  # query set -- pk : Primary Key
    if item.quantity == 0:
        messages.warning(request, item.name + ' is out of stock.')
    else:
        item.quantity -= 1
        item.save()
        messages.success(request, item.name + ' was successfully rented.')
    return redirect('mysite:rental')


def remove(request, item_id):
    item = Bounce.objects.get(pk=item_id)  # query set -- pk : Primary Key
    if item.quantity == 20:
        return redirect('mysite:rental')
    else:
        item.quantity += 1
        item.save()
        messages.success(request, item.name + ' was successfully returned.')
    return redirect('mysite:rental')
