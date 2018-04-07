# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import User

def index(request):
    context= {
        'users': User.objects.all()
    }
    return render(request, "semi_app/index.html", context)

def new(request):
    return render(request, "semi_app/new.html")

def create(request):
    User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'],email = request.POST['email'])
    return redirect('/users')

def edit(request, user_id):
    context= {
        'users': User.objects.get(id = user_id)
    }
    return render(request,'semi_app/edit.html', context)

def update(request, user_id):
    updates = User.objects.get(id = user_id)
    updates.first_name = request.POST['first_name']
    updates.last_name = request.POST['last_name']
    updates.email = request.POST['email']
    updates.save()
    return redirect('/users')

def show(request, user_id):
    context= {
        'users': User.objects.get(id = user_id)
    }
    return render(request,'semi_app/show.html', context)

def delete(request, user_id):
    b = User.objects.get(id=user_id)
    b.delete()
    return redirect('/users')
