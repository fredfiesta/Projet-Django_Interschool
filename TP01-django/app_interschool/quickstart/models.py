# Create your models here.
from django.db import models


class Event(models.Model):
    date_de_creation = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length=100, blank=True, default='')
    desc = models.TextField()

    class Meta:
        ordering = ['date_de_creation']
