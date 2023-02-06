from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

from SearchApp.models import Videos
from SearchApp.serializers import VideosSerializer
from rest_framework.generics import ListAPIView
from .pagination import customPagination

class VideosApi(ListAPIView):
    queryset = Videos.objects.raw('SELECT * FROM public."SearchApp_videos" ORDER BY "UploadTime" DESC')
    serializer_class = VideosSerializer
    pagination_class = customPagination

@csrf_exempt
def SearchApi(request, id=0):
    if request.method == 'GET':
        return HttpResponse("Send POST requests to Search videos")
    if request.method == 'POST':
        query = JSONParser().parse(request)
        search_query = query['data']
        search_query = "%"+search_query+"%"
        videos = Videos.objects.raw('SELECT * FROM public."SearchApp_videos" WHERE "VideoTitle" LIKE %s', [search_query])
        videos_serializer = VideosSerializer(videos, many=True)
        return JsonResponse(videos_serializer.data, safe=False)
    

