from django.shortcuts import render

# Create your views here.
def f1(request):
    return render(request,'MyApps1/child.html')
def f11(request):
    return render(request,'MyApps1/child1.html')