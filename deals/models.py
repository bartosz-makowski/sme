from django.db import models


class Deal(models.Model):
    name = models.CharField(max_length=65)
    price = models.IntegerField(max_length=3)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
