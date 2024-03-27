from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('itinerary/', views.itinerary, name='itinerary'),
]
