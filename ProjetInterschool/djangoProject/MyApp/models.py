from datetime import date

import django.contrib.auth.models
from django.db import models

class Event(models.Model):
    id = models.IntegerField
    nom = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=200)
    heure = models.DateTimeField()

class Lieu(models.Model):
    nom = models.CharField(max_length=50)


class Commentaire(models.Model):
    contenu = models.CharField(max_length=50)
    date = models.DateField()
    heure = models.DateTimeField()

class CommentaireLieu(models.Model):
    contenu = models.CharField(max_length=50)
    date = models.DateField()
    heure = models.DateTimeField()
