# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import Course

# Create your views here.
def index(request):
    #print "HI"
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)
def add(request):
    results = Course.objects.val(request.POST)
    if results['status'] == False:
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')
def remove(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'course_app/delete.html', context)
def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')