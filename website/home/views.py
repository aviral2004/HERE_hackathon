from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'pages/custom-home.html')
    return render(request, 'pages/custom-index.html')

def home(request):
    return render(request, 'pages/custom-home.html')

def main(request):
    return render(request, 'pages/custom-main.html')

def itinerary(request):
    return render(request, 'pages/custom-itinerary.html')
