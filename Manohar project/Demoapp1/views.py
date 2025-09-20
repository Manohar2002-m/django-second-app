from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    ss="<h1> Welcome to Django First Project(DJMyFirstProject) & FirstApp(my Apps)<h1/><hr/>"
    return HttpResponse(ss)
def show (request):
    ss="<h2> we want to meet Hardik Pandya on 17th april<h2><hr/>"
    return HttpResponse(ss)
def hello(request):
    ss="<h3>Iam Going to college on Sunday for the Review purpose<h3/>"
    ss="<h3>color:blue<h3/><hr/>"
    return HttpResponse(ss)