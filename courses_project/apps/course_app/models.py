# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def val(self, data):
        results = {"status": True, "errors":[]}
        if len(data['name']) < 5:
            results['errors'].append('course name must be longer than 5 chars')
        if len(data['desc']) < 15:
            results['errors'].append('description must be longer than 15 chars')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()