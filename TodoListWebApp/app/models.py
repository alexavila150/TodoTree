"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Task(models.Model):
    name = models.fields.CharField(max_length=20)
    due_date = models.fields.DateTimeField()
