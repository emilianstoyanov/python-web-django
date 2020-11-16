from django.contrib import admin

# Register your models here.
from pets.models import Like, Pet

admin.site.register(Like)
admin.site.register(Pet)
