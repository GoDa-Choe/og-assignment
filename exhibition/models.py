from django.db import models

from collection.models import Artist, Artwork


class Exhibition(models.Model):
    title = models.CharField(max_length=64)
    start_date = models.DateField(help_text='YYYY-MM-DD')
    end_date = models.DateField(help_text='YYYY-MM-DD')

    poster = models.ImageField(null=True, blank=True, upload_to='exhibition/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ForeignKey
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    artworks = models.ManyToManyField(Artwork)
