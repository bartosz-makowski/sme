from django.db import models


class Day(models.Model):
    date = models.DateField(auto_now=False,
                            auto_now_add=False, primary_key=True)


class Time(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.CharField(max_length=12)