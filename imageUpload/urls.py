from os import name
from django.conf.urls import url
from django.urls.conf import include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'imageprocess', views.imageProcess, name='imageprocess')
]
