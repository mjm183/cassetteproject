from django.db import models

# Create your models here NIGGER

class Tape(models.Model):
    title = models.CharField()
    artist = models.ManyToManyField(Artist)
    year = models.CharField()
    label = models.ManyToManyField(Label)


class Artist(models.Model):
    artistname = models.CharField()


class Label(models.Model):
    labelname = models.CharField()