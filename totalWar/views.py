from django.shortcuts import render

# Create your views here.
def homepageTW(request):
    return render(request, "homepageTW.html", {})