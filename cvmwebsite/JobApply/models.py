from django.db import models
from django import forms


# Create your models here.
class JA(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=200)
    current_location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    langguage = models.CharField(max_length=200)
    about_me = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    img =models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.first_name