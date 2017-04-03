from django.shortcuts import render, redirect
from .models import Bounce
from .forms import BounceIntoFun

# Create your views here.


def home(request):
    return render(request, 'Rent/home.html')


def contact(request):
    return render(request, 'Rent/contact.html')


def view_form(request):
    if request.method == 'GET':
        bouncers = Bounce.objects.all()
        form = BounceIntoFun()
        return render(request, 'Rent/rental.html', {'form': form,
                                                    'bouncers': bouncers})
    else:
        form = BounceIntoFun(request.POST)
        print(form)
        return redirect('rental')
