from django.shortcuts import render
def wishes(request):
    return render (request,'FirstApp/wishes.html')
def hello(request):
    return render(request,'FirstApp/hello.html')
