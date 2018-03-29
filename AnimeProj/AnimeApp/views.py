
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .animeModels import Anime

# Create your views here.
def index(request):
    listing = Anime.readAll()
    args={
        'animes': Anime.objects.all()
    }

    return render(request,'list.html', args)