from django.db import models

# Create your models here
# Written by Kyle and Michael on 02/21/15

class Tape(models.Model):
    title = models.CharField()
    artist = models.ManyToManyField(Artist)
    year = models.CharField()
    label = models.ManyToManyField(Label)


class Artist(models.Model):
    artistname = models.CharField()


class Label(models.Model):
    labelname = models.CharField()