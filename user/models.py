from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

# Create your models here.
class User(AbstractUser):
    phone = PhoneField(blank=True, help_text='Contact phone number')
    address = models.URLField(max_length=250)