from django.contrib import admin
from exhibition import models


@admin.register(models.Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'created_at']
