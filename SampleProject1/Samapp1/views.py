from django.shortcuts import render
from django.http import HttpResponse
def f11(request):
    return HttpResponse("<h1> Hello World! from Samapp1 f11() </h1><hr />")
def f22(request):
    return HttpResponse("<h1> Hello World! from Samapp1 f22() </h1><hr />")

# Create your views here.
