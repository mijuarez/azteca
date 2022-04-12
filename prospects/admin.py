from django.contrib import admin
from .models import Prospecters

@admin.register(Prospecters)
class ProspectersAdmin(admin.ModelAdmin):
    pass