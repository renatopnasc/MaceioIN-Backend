from django.contrib import admin
from .models import Setor

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ["nome"]