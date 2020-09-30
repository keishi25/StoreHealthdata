from django.db import models
from django import forms
from django.utils import timezone


# Personal master data.
class Person(models.Model):
    # user_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=100, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=20, null=True)


# HealthData
class HealthData(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    weight = models.CharField(max_length=20)
    fat = models.CharField(max_length=20, blank=True)
    muscle_mass = models.CharField(max_length=20, blank=True)
    memo = models.TextField(blank=True)

# サンプル
from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)

    def get_absolute_url(self):
      return reverse('author-detail', kwargs={'pk': self.pk})
