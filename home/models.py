from django.db import models


class Location(models.Model):
    description = models.TextField()
    image = image = models.ImageField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
