from django.conf.urls import url
from . import views

app_name = 'mysite'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^rental$', views.view_form,
        name='rental'),
    url(r'^contact$', views.contact,
        name='contact'),
    url(r'^rent/(?P<item_id>[0-9]+)/$',
        views.rent, name='rent'),
    url(r'^remove/(?P<item_id>[0-9]+)/$',
        views.remove,
        name='remove'),
]

# r'^home$' = expressions
# ^ beginning of str
# $ end of str
