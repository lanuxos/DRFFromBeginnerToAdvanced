# DRF From Beginner to Advanced
# EP7 - Views (Continous)
```
from django.shortcuts import render
from .models import *
from django.http import JsonResponse, response

def Test(request):
    return response.HttpResponse("<h1>Matabase API</h>")

def TestAgain(request):
    return JsonResponse("<h1>Matabase API again</h>", safe=False)

def TestMethod(request):
    method = request.method.lower()
    if method == "get":
        return JsonResponse("getting data")
    elif method == "post":
        return JsonResponse("posting data")
    elif method == "put":
        return JsonResponse("updating data")
    elif method == "delete":
        return JsonResponse("deleting data")
    elif method == "patch":
        return JsonResponse("patching not allowed")


from rest_framework.views import APIView
from django.forms.models import model_to_dict

class SimpleAPI(APIView):
    def post(self, request):
        title = request.data['title']
        year = request.data['year']
        newData = MatabaseModel.objects.create(title=title, year=year)
        return JsonResponse({"data": model_to_dict(newData)})
    def get(self, request):
        matabases = MatabaseModel.objects.all().values()
        print(matabases)
        return JsonResponse({"data": list(matabases)})
```
```
"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from matabase.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', Test),
    path('testagain/', TestAgain),
    path('testmethod/', TestMethod),
    path('simpleapi/', SimpleAPI.as_view()),
]

```