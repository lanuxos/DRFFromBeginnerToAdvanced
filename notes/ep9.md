# DRF From Beginner to Advanced
# EP9 - Serializers APIView [get, post]
```
from rest_framework import serializers

class SimpleAPISerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    status = serializers.CharField()
    createdDate = serializers.DateTimeField(read_only=True)
    updatedDate = serializers.DateTimeField(read_only=True)
```
```
from .models import *
from django.http import JsonResponse, response
from rest_framework.views import APIView
from .serializers import SimpleAPISerializer

class SimpleAPI(APIView):
    def post(self, request):
        serializer = SimpleAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = request.data['title']
        year = request.data['year']
        newData = MatabaseModel.objects.create(title=title, year=year)
        return JsonResponse({"data": SimpleAPISerializer(newData).data})
    def get(self, request):
        matabases = MatabaseModel.objects.all()
        return JsonResponse({"data": SimpleAPISerializer(matabases, many=True).data})
```