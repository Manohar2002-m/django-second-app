from django.urls import path	#new
from Samapp1 import views

urlpatterns = [
	path('first/', views.f11),
	path('second/', views.f22),
]
