from django.shortcuts import render
from data.models import Adult
# Create your views here.

def homepageFE(request):
    return render(request, "homepageFE.html", {})


def adults(request):
    return render(request, "adults.html", {"Males": Adult.objects.filter(sex = "M"), "objects": Adult.objects.all(), "Females": Adult.objects.filter(sex = "F")})


def calc(request):
    if(calc.GET.get('button')):

        return render(request, "calc.html", {})


def home(request):
    return render(request, "home.html", {})