from django.contrib import admin

# Register your models here.
from .models import Artiste, Song, lyric


admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)