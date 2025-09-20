from django.contrib import admin

# Register your models here.
from ManuApp.models import Movies
class MoviesAdmin(admin.ModelAdmin):
    list_display=['moviename','actorname','actressname','releasedate','movierating']
admin.site.register(Movies,MoviesAdmin)