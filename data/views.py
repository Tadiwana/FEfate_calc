from django.shortcuts import render

# Create your views here.

def homepageFE(request):
    return render(request, "homepageFE.html", {})


def practice(request):
    return render(request, "Practice.html", {})

def home(request):
    return render(request, "home.html", {})