# paymetns/urls.py  

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('charge/',views.charge,name='charge')
]