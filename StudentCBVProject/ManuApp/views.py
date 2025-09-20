from django.shortcuts import render
from django.urls import reverse_lazy
from ManuApp.models import Student

# Create your views here.
from django.views.generic import ListView,DetailView
class StudentListView(ListView):
    model=Student

class StudentDetailview(DetailView):
    model=Student

from django.views.generic import CreateView,UpdateView,DeleteView
class StudentCreateView(CreateView):
    model=Student
    fields=('no','name','marks','total');
class StudentUpdateView(UpdateView):
    model=Student
    fields=('name','marks');
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('list')


    
