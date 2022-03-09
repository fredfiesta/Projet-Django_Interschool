# Create your models here.
from django.db import models


class Event(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    titre = models.CharField(max_length=100, blank=True, default='*pas de titre déterminé')
    lieu = models.CharField(max_length=100, blank=True, default='*pas de lieu déterminé')
    desc = models.TextField()

    class Meta:
        ordering = ['date']
