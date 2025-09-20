from django.contrib import admin
from MovieApp.models import Movies
class MoviesAdmin(admin.ModelAdmin):
    list_display=['releasedate','moviename','actorname','actressname','rating',];
admin.site.register(Movies,MoviesAdmin);

# Register your models here.
