from .models import *
from .serializers import SimpleAPISerializer
from rest_framework import viewsets

    
class SimpleAPIViewset(viewsets.ModelViewSet):
    queryset = MatabaseModel.objects.all()
    serializer_class = SimpleAPISerializer