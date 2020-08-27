from django.urls import path

from . import views

urlpatterns = [
    path('recode', views.recode, name='recode'),
    path('recode_person', views.recode_person, name='recode_person'),
]