from django.contrib import admin

# Register your models here.
from .animeModels import Anime

#shows Anime class on django admin page
admin.site.register(Anime)