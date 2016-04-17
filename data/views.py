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
    mylist=[father.name, (Decimal(mother.hpG) + Decimal(father.hpG))/2, (Decimal(mother.strG) + Decimal(father.strG))/2,(Decimal(mother.magG) + Decimal(father.magG))/2,(Decimal(mother.skillG) + Decimal(father.skillG))/2,(Decimal(mother.spdG) + Decimal(father.spdG))/2, (Decimal(mother.lckG) + Decimal(father.lckG))/2, (Decimal(mother.defG) + Decimal(father.defG))/2, (Decimal(mother.resG) + Decimal(father.resG))/2, (int(mother.strB) + int(father.strB) + 1),(int(mother.magB) + int(father.magB) + 1),(int(mother.skillB) + int(father.skillB) + 1), (int(mother.spdB) + int(father.spdB) + 1),(int(mother.lckB) + int(father.lckB) + 1),(int(mother.defB) + int(father.defB) + 1),(int(mother.resB) + int(father.resB) + 1)]
    # HPg = (Decimal(mother.hpG) + Decimal(father.hpG))/2
    # STRg=
    # MAGg=
    # SKLg=
    # SPDg=
    # LCKg=
    # DEFg=
    # RESg=
    # STRb=
    # MAGb=
    # SKLb=
    # SPDb=
    # LCKb=
    # DEFb=
    # cp=
    # c2=
    # c=newChild(name = "something", nonvariableParent = father.name , hpG = HPg, strG = STRg,magG = MAGg, skillG =SKLg, spdG = SPDg, lckG =LCKg, defG=DEFg, resG=RESg, strB = STRb, magB= MAGb, skillB=SKLb, spdB = SPDb, lckB = LCKb, defB = DEFb, resB = RESb,  classP =cp, class2 = c2))
    # c.save()
    return mylist
def child(request):
    form = ChildForm(request.GET)
    form.is_valid()
    mother_id = form.cleaned_data['mother']
    father_id = form.cleaned_data['father']
    mother = Adult.objects.filter(id=mother_id).first()
    father = Adult.objects.filter(id=father_id).first()

    child = calculate(mother=mother, father=father)

    print(str(form.cleaned_data))
    return render(request, "child.html", {"objects": Adult.objects.all(), "child": child})

class ChildForm(forms.Form):
    father = forms.ChoiceField(label="father", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "M")])
    mother = forms.ChoiceField(label="mother", choices=[ (adult.id, adult.name) for adult in Adult.objects.filter(sex = "F")])

