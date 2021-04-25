from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
