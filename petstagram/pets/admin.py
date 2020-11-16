from django.contrib import admin

# Register your models here.
from pets.models import Like, Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')


admin.site.register(Like)
admin.site.register(Pet, PetAdmin)
