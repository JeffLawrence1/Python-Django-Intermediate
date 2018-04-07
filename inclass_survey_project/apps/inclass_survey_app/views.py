# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "inclass_survey_app/index.html")

def info(request):
    request.session['name'] = request.POST['name']
    return redirect('/')