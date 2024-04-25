# DRF From Beginner to Advanced
# EP3 - Model
```
from django.db import models

class Matabase(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    statusOption = (
        ('d', 'Downloaded'),
        ('w', 'Watched'),
        ('r', 'Removed')
    )
    status = models.CharField(max_length=10, choices=statusOption, default='d')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} / {self.year} / {self.status}"
```