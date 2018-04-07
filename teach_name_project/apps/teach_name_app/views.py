# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Adder

# Create your views here.
def index(request):
    return render(request, "teach_name_app/index.html")

def add(request):
    Adder.objects.create(name=request.POST['name'])
    return redirect('/landing')

def landing(request):
    context = {
        "rays": Adder.objects.filter(name='ray').count(),
        "others": Adder.objects.all().exclude(name="ray"),
    }
    return render(request, "teach_name_app/landing.html", context)
