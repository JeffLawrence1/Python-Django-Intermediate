# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GuestManager(models.Manager):
    def val(self, postData):
        results = {'errors': []}
        if len(postData['name']) < 3:
            results['errors'].append('Your first name must be 3 chars')
        
        return results


class Guest(models.Model):
    name = models.CharField(max_length=111)
    objects = GuestManager()