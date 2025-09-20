from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    return HttpResponse("<h1> Helllo User welcome to Django Project </h1> <hr/>")
