from django.contrib import admin
from .models import Anime

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('TITLE', 'DESCR', 'IMGPATH', 'SHOWN')

admin.site.register(Anime, AnimeAdmin)
