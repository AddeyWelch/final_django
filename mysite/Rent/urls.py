from django.conf.urls import url
from . import views

app_name = 'mysite'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^rental$', views.view_form,
        name='rental'),
    url(r'^contact$', views.contact,
        name='contact'),
    url(r'^cart/$', views.view_form, name='cart'),
]

# r'^home$' = expressions
# ^ beginning of str
# $ end of str
