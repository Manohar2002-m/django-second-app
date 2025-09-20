from django.urls import path;
from Demoapp1 import views;

urlspatterns= [
    path ('first/',views.f1),
    path('second/',views.f2),
    ];