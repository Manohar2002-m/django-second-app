from django.shortcuts import render

# Create your views here.
from ManuApp.forms import MoviesForm
from ManuApp.models import Movies

def index_view(request):
    return render(request,'ManuApp/index.html')


def add_movie_view(request):
    formObj = MoviesForm()
    if request.method == "POST":
        formObj = MoviesForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['releasedate'])
            print(formObj.cleaned_data['moviename'])
            print(formObj.cleaned_data['actorname'])
            print(formObj.cleaned_data['actressname'])
            print(formObj.cleaned_data['movierating'])
            formObj.save()  # auto-commit
            return index_view(request)
    return render(request, 'ManuApp/addmovie.html', {'form1': formObj})


def list_movie_view(request):
    movies_list = Movies.objects.all().order_by('-rating')  # (-)desc-order
    return render(request, 'ManuApp/listmovie.html', {'movies_list': movies_list})






