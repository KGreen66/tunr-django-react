from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=400, null=True, blank=True) #null is db related; blank is validation (forms)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    preview_url = models.CharField(max_length=400)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs') #Related name is what this model will be referred to in the foreign key model ie Artist

    def __str__(self):
        return self.title