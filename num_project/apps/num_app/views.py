# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "num_app/index.html")

def add(request):
    num1 = request.POST['number1']
    num2 = request.POST['number2']
    # num1 = int(num1[0])
    # num2 = int(num2[0])
   
    # request.session['number1'] = request.POST['number1']
    # request.session['number2'] = request.POST['number2']
    try:
        result = int(num1) + int(num2)
    # result = int(result)
    # print result
    except ValueError:
        messages.error(request, "must enter numbers in the boxes")
        return redirect('/')
    # if not request.POST['number1'].isdigit() or request.POST['number2'].isdigit():
    #     messages.error(request, "must enter numbers in the boxes")
    #     return redirect('/')
    # else:
    # request.session['result'] = result
        # result = request.session['number1'] + request.session['number2']
    context = {
        "result": result,
    }
    return render(request, "num_app/landing.html", context)