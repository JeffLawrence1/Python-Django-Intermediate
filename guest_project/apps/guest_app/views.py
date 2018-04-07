# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User

# Create your views here.
def index(request):
    return render(request, "guest_app/index.html")

def create(request):
    u = User.objects.create(name=request.POST['name'])
    return redirect('/landing')

def landing(request):
    context = {
        "names": User.objects.all()
    }
    return render(request, "guest_app/landing.html", context)