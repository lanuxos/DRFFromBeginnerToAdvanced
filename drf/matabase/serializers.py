from rest_framework import serializers
from .models import *


class SimpleAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = MatabaseModel
        fields = ("__all__")