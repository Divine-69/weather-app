from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "weather/index.html")

def single(request):
    return render(request, "weather/single.html")

def news(request):
    return render(request, "weather/news.html")

def photos(request):
    return render(request, "weather/photos.html")

def live_cameras(request):
    return render(request, "weather/live-cameras.html")

def contact(request):
    return render(request, "weather/contact.html")
