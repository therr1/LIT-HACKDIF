from django.contrib import admin

from .models import UserProfile, RentableObject
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(RentableObject)