from django.shortcuts import render
from .models import Playlist



def index(request):
    playlist_songs = Playlist.objects.all()
    context = {'playlist_songs': playlist_songs}
    return render(request, 'playlist/main_page.html', context)