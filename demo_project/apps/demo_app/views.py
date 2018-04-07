# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
# print User
# Create your views here.
def index(request):
    return render(request, "demo_app/index.html")

def process(request):
    User.objects.create(first_name= request.POST['first_name'])
    # print request.POST['first_name']
    context = {
        "users": User.objects.all()
    }
    return render(request, "demo_app/landing.html", context)