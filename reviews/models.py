from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=50, null=False,
                             blank=False, default='Title')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20, null=False, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.title
