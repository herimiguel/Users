from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=101)
  last_name = models.CharField(max_length=101)
  email_address = models.CharField(max_length=101)
  age = models.IntegerField()
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

