from django.db import models

# Create your models here.

class Videos(models.Model):
    VideoId = models.CharField(primary_key=True, max_length = 50)
    VideoTitle = models.CharField(max_length = 200)
    VideoDescription = models.CharField(max_length = 500)
    UploadTime = models.DateTimeField()
    ThumbnailURL = models.URLField()
    
    class Meta:
        indexes = [
            models.Index(fields=['-UploadTime',], name='datetime_desc_idx')
        ]