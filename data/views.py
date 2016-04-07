from django.shortcuts import render
from data.models import Adult
# Create your views here.

def homepageFE(request):
    return render(request, "homepageFE.html", {})


def adults(request):
    return render(request, "adults.html", {"objects": Adult.objects.order_by("name")})

def home(request):
    return render(request, "home.html", {})