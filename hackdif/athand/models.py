from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserProfile (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    home_location = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    user_name = models.CharField(max_length=20)


class RentableObject (models.Model):
    user_name = models.CharField(max_length=20)
    name = models.CharField(max_length=100)





