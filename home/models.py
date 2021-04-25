from django.db import models


class Location(models.Model):
    description = models.TextField()
    image = image = models.ImageField(null=False, blank=False)

