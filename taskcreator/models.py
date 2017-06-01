# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # personal information about the merchant
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=500, blank=True)
    deadline = models.DateField()
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.username