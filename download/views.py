from django.shortcuts import render

from download.models import Music

# Create your views here.


def download_display(request):
    musics = Music.get_musics()
    musics_length = len(musics)

    return render(request,
                  'download/download_display.html',
                  {'musics': musics,
                   'length': musics_length})
