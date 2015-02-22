from django.db import models

# Create your models here
# Written by Kyle and Michael on 02/21/15

#Add Genre

class Artist(models.Model):
    artistname = models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.artistname)


class Label(models.Model):
    labelname = models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.labelname)


class Tape(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField(Artist)
    year = models.CharField(max_length=100)
    labels = models.ManyToManyField(Label)


