__author__ = 'mslavin'
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home', views.home, name='home'),  # ex: /polls/
    url(r'^create', views.create, name='create'),
    url(r'^contact', views.contact, name='contact'),
]
