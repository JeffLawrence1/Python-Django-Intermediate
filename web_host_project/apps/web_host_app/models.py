# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    
    def val(self, postData):
        results = {"errors": []}
        if not postData['name'].startswith("www"):
            results['errors'].append('address must start with www')
        if not postData['name'].endswith(".com"):
            results['errors'].append('address must end with .com')
        if User.objects.filter(name=postData['name']).count() > 0:
            results['errors'].append('name already taken come up with your own ideas!')
        return results

    def checkVal(self, postData):
        results = {"errors": []}        
        if User.objects.filter(name=postData['name']).count() > 0:
            results['errors'].append('name taken!')
        if User.objects.filter(name=postData['name']).count() == 0:
            results['errors'].append('name available!')
        return results

class User(models.Model):
    name = models.CharField(max_length=111)
    objects = UserManager()