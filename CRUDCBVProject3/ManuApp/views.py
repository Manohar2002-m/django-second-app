from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from ManuApp.forms import StudentForm
from ManuApp.models import Student

# Create your views here.
def show_view(request):
    students= Student.objects.all()
    return render(request, 'ManuApp/index.html', {'students': students})

def insert_view(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request, "ManuApp/insert.html", {"form":form})


def delete_view(request,pk):        #use pk only here (same as url)
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('/index')

def update_view(request,pk):    #use pk only here(same as url)
    student=Student.objects.get(id=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/index')
    return render(request,'ManuApp/update.html',{'student':student})



