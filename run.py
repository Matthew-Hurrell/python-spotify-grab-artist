import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

"""
SPOTIPY_CLIENT_ID = "7ba153190c884278957b14d76473e624"
SPOTIPY_CLIENT_SECRET = "d41061364f1b40c681bdf30d5b87d8c8"
SPOTIPY_REDIRECT_URI = "https://localhost:8000/callback"
"""

uri = 'spotify:artist:7jy3rLJdDQY21OgRLCZ9sD'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

i = 1
while(i < len(albums)):
    for album in albums:
        print(f"{i}. {album['name']}")
        i += 1