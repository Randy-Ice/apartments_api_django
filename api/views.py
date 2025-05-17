from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blah(request):
    return HttpResponse('Hello world')