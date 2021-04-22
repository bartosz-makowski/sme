from django.db import models


class Day(models.Model):
    date = models.DateField(auto_now=False,
                            auto_now_add=False, primary_key=True)
