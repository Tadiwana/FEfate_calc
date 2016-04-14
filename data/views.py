from django.shortcuts import render
from data.models import Adult
from django import forms
# Create your views here.

def homepageFE(request):
    return render(request, "homepageFE.html", {})


def adults(request):
    form = ChildForm()
    return render(request, "adults.html", {'form': form})


def calc(request):
    #if(calc.GET.get('button')):

    return render(request, "calc.html", {"Males": Adult.objects.filter(sex = "M"), "objects": Adult.objects.all(), "Females": Adult.objects.filter(sex = "F")})


def home(request):
    return render(request, "home.html", {})

# def calculate(mother, father):

def child(request):
    form = ChildForm(request.GET)
    form.is_valid()
    mother_id = form.cleaned_data['mother']
    father_id = form.cleaned_data['father']
    mother = Adult.objects.filter(id=mother_id).first()
    father = Adult.objects.filter(id=father_id).first()
   # child = calculat(mother=mother, father=father)

    print(str(form.cleaned_data))
    return render(request, "child.html", {"objects": Adult.objects.all(), child: child})

class ChildForm(forms.Form):
    father = forms.ChoiceField(label="father", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "M")])
    mother = forms.ChoiceField(label="mother", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "F")])

