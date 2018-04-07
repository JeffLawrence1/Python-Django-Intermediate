# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import Guest
# Create your views here.
def index(request):
    return render(request, "guest_book_app/index.html")

def add(request):
    results = Guest.objects.val(request.POST)
    for error in results['errors']:
        messages.error(request, error)
        return redirect('/')

    Guest.objects.create(name=request.POST['name'])

    return redirect('/landing')

def landing(request):
    context = {
        "guest": Guest.objects.all()
    }
    return render(request, "guest_book_app/landing.html", context)