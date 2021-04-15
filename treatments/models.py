from django.db import models


class Treatment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False),
    description = models.TextField(),
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
