from django.contrib import admin

from collection import models


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'birth', 'email', 'phone_number', 'user', 'is_confirmed', 'created_at']


@admin.register(models.Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'artist', 'canvas_size', 'price', 'created_at']
