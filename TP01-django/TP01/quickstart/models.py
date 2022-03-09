# Create your models here.
from django.db import models


class Event(models.Model):
    date_de_creation = models.DateTimeField(auto_now_add=True)
    nom_de_event = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['date_de_creation']
