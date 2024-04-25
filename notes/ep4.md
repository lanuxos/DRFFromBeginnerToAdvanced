# DRF From Beginner to Advanced
# EP4 - Model(Continuous)
```
from django.contrib import admin
from .models import Matabase

admin.site.register(Matabase)
```
```
from django.db import models
from django.utils import timezone

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
        return f"{self.title} / {self.year} / {self.status} / {self.updatedDate.strftime('%Y%m%d-%H%M%S')}"
    
    class Meta:
        ordering = ('-updatedDate', '-createdDate')

```