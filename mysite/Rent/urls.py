from django.conf.urls import url
from . import views

app_name = 'BounceIntoFun'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^rental$', views.rental, name='rental'),
    url(r'^contact$', views.contact,
        name='contact'),
]
