# DRF From Beginner to Advanced
# EP5 - Model (final)
```
from django.db import models
from django.utils import timezone

class Matabase(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, editable=False, default="null")
    year = models.IntegerField()
    statusOption = (
        ('d', 'Downloaded'),
        ('w', 'Watched'),
        ('r', 'Removed')
    )
    status = models.CharField(max_length=10, choices=statusOption, default='d')
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.title} / {self.year} / {self.status} / {self.updatedDate.strftime('%Y%m%d-%H%M%S')}"
    def __str__(self):
        return self.description
    
    class Meta:
        ordering = ('-updatedDate', '-createdDate')
        verbose_name_plural = "Matabase"

    def save(self, *args, **kwargs):
        self.description = f"{self.title} / {self.year} / {self.status}"
        super().save(*args, **kwargs)
class Mag(models.Model):
    magRef = models.ForeignKey(Matabase, on_delete=models.CASCADE, related_name='mag_references')
    mag = models.CharField(max_length=255)

    def __str__(self):
        return self.magRef.title + ' / ' + self.mag
```