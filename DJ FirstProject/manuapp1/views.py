from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f1(request):
    return HttpResponse("<h1 style='color:Pink;'> Pesala Manohar Reddy</h1> <hr/>")
def f2(request):
    return HttpResponse("<h2  style='color:green;'> Iam Studying at Vikrama Simhapuri University at Nellore<h2><hr/>")
def f3(request):
    return HttpResponse("<h3  style =' color: violet;'> Iam Pursing MCA Final Year<h3><hr/>")