from django.db import models
from django.utils import timezone
# Create your models here.
class Meme(models.Model):
    name = models.CharField(max_length=200)
    caption = models.TextField()
    url = models.URLField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    