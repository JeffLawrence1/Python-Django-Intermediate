# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Cat, Dog

# Create your views here.
def index(request):
    return render(request, "pet_app/index.html")

def pet(request):
    pet = request.POST['pet']
    # print pet
    if pet == "cat":
        Cat.objects.create(name=request.POST['name'])
    elif pet == "dog":
        Dog.objects.create(name=request.POST['name'])
    return redirect('/landing')

def landing(request):
    context = {
        "cats": Cat.objects.all(),
        "dogs": Dog.objects.all(),
    }
    return render(request, "pet_app/landing.html", context)