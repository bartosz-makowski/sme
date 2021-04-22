from django.db import models


class Day(models.Model):
    date = models.DateField(auto_now=False,
                            auto_now_add=False, primary_key=True)

    def __str__(self):
        return self.date


class Time(models.Model):
    date = models.ForeignKey(Day, on_delete=models.CASCADE)
    time = models.CharField(max_length=12)

    def __str__(self):
        return self.time