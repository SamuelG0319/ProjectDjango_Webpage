from django.contrib import admin    #importo la librería de admin desde django

#importamos los modelos creados en el archivo models
from . models import (
    ContactProfile,
    Blog,
    Review
    )

#Registro en admin todos los modelos creados con los datos que quiero ver
@admin.register(ContactProfile)                     #Registro en admin el modelo ContactProfile
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)

@admin.register(Blog)                               #Registro en admin el modelo Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    readonly_fields = ('slug',)                     #Le agrego el slug como un campo solo para lectura

@admin.register(Review)                             #Registro el modelo de Review
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    readonly_fields = ('slug',)                     #Le agrego el slug como un campo solo para la lectura

# Register your models here.
