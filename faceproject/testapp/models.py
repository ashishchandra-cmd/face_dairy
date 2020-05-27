from django.db import models
from django.utils import timezone
# Create your models here.
class face(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    img=models.ImageField(upload_to='images')
    publish=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title        