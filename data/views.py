from django.shortcuts import render
from data.models import Adult, Child, newChild
from django import forms
from decimal import *
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

def calculate(mother, father):


    hp = ( int(mother.hpG) + int(father.hpG)) / 2
    str = ( int(mother.strG) + int(father.strG)) / 2
    mag = ( int(mother.magG) + int(father.magG)) / 2
    skill = ( int(mother.skillG) + int(father.skillG)) / 2
    spd = ( int(mother.spdG) + int(father.spdG)) / 2
    lck = ( int(mother.lckG) + int(father.lckG)) / 2
    defG = ( int(mother.defG) + int(father.defG)) / 2
    res = ( int(mother.resG) + int(father.resG)) / 2
    stats = ["child", hp, str, mag, skill, spd, lck, defG, res, (int(mother.strB) + int(father.strB) + 1),(int(mother.magB) + int(father.magB) + 1),(int(mother.skillB) + int(father.skillB) + 1), (int(mother.spdB) + int(father.spdB) + 1),(int(mother.lckB) + int(father.lckB) + 1),(int(mother.defB) + int(father.defB) + 1),(int(mother.resB) + int(father.resB) + 1)]
    return stats

def child(request):
    form = ChildForm(request.GET)
    form.is_valid()
    mother_id = form.cleaned_data['mother']
    father_id = form.cleaned_data['father']
    mother = Adult.objects.filter(id=mother_id).first()
    father = Adult.objects.filter(id=father_id).first()

    child = calculate(mother=mother, father=father)


    print(str(form.cleaned_data))
    return render(request, "child.html", {"objects": Adult.objects.all(), "child": child, "mother": mother, "father": father})


class ChildForm(forms.Form):
    father = forms.ChoiceField(label="father", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "M")])
    mother = forms.ChoiceField(label="mother", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "F")])

