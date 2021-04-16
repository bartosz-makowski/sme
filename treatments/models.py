from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
