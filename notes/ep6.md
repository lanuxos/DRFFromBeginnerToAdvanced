# DRF From Beginner to Advanced
# EP6 - Views
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
```