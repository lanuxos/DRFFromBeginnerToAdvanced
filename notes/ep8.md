# DRF From Beginner to Advanced
# EP8 - Serializers introduction
```
from rest_framework import serializers

class SimpleObject():
    def __init__(self, title):
        self.title = title


class SimpleObjectSerializer(serializers.Serializer):
    title = serializers.CharField()

def run_data():
    simple_var = SimpleObject("Sweet December")
    simple_var_serializer = SimpleObjectSerializer(simple_var)
    print(simple_var_serializer.data)
```