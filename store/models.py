from django.db import models
from django import forms


# Personal master data.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
   #email_address = forms.EmailField(max_length=250)
    #birth = models.CharField(max_length=20)
    #sex = models.CharField(max_length=20)


# HealthData
class HealthData(models.Model):
    #user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    #date = models.DateTimeField()
    #time = models.DateTimeField()
    weight = models.CharField(max_length=20)
    #fat = models.CharField(max_length=20, blank=True)
    #muscle_mass = models.CharField(max_length=20, blank=True)
    #memo = models.TextField(blank=True)

