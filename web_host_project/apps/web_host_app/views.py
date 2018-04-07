# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
# Create your views here.
def index(request):
    return render(request, "web_host_app/index.html")

def add(request):
    results = User.objects.val(request.POST)
    for error in results['errors']:
        messages.error(request, error)
        return redirect('/')

    User.objects.create(name=request.POST['name'])

    return redirect('/landing')

def checker(request):
    results = User.objects.checkVal(request.POST)
    for error in results['errors']:
        messages.error(request, error)
        return redirect('/')
    
def landing(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "web_host_app/landing.html", context)