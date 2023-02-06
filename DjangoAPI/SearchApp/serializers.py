from rest_framework import serializers
from SearchApp.models import Videos

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields=('VideoId', 'VideoTitle', 'VideoDescription', 'UploadTime', 'ThumbnailURL')