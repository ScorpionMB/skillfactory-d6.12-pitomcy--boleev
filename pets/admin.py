from django.contrib import admin
from .models import Breed, Pet


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'type_of_animal','breed', 'color', 'data')
    list_display_links = ('breed', 'name')
    search_fields = ('name', 'breed')

