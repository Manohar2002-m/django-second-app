from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f3(request):
    return HttpResponse("<h1> Hello from Demoapp2 f3() </h1> <hr />")
def f4(request):
    return HttpResponse("<h1> Hello from Demoapp2 f4() </h1> <hr />")