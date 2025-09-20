from django .shortcuts import render
from ManuApp.forms import LoginForm
import datetime;
#Create your views here.
def home_view(request):
    formobj=LoginForm()
    return render(request,'ManuApp/home.html',{'formobj':formobj})

def date_time_view(request):
    #form=LoginForm(request.GET)
    name=request.GET['name']
    response=render(request,'ManuApp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response;

def result_view(request):
    name = request.POST["name"]
    date_time=datetime.datetime.now()
    dict1={'name':name,'date_time':date_time}
    return render(request, 'ManuApp/result1.html', dict1)


##Application-3
from django.shortcuts import render
# Create your views here.
def name_view(request):
    return render(request,'ManuApp/name.html');


def age_view(request):
    name = request.GET['name']
    response = render(request,'ManuApp/age.html', {'name': name})
    response.set_cookie('name', name)
    return response


def parent_view(request):
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request,'ManuApp/parent.html', {'name': name})
    response.set_cookie('age', age)
    return response


def result1_view(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    pname = request.GET['pname']
    response = render(request,'ManuApp/result1.html', {'name': name, 'age': age, 'pname': pname})
    response.set_cookie('pname', pname)
    return response



