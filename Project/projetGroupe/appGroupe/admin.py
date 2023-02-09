# Register your models here.
from django.contrib import admin
from .models import *

@admin.register(Bachelier)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom','genre', ) 
    ordering = ('nom', )
    search_fields = ('nom', ) 
@admin.register(Conseiller_orientation)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('nom','genre', 'grade', ) 
    ordering = ('nom', )
    search_fields = ('nom', ) 
@admin.register(Adresse)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email','quartier', 'ville', ) 
    ordering = ('email', )
    search_fields = ('email', ) 
@admin.register(Dossier)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('numero_dossier', ) 
    ordering = ('numero_dossier', )
    search_fields = ('numero_dossier', )
@admin.register(EntiteRessource)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('adresse', ) 
    ordering = ('nom', )
    search_fields = ('nom', )


# Register your models here.

# Register your models here.
