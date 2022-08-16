import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

"""
SPOTIPY_CLIENT_ID = "7ba153190c884278957b14d76473e624"
SPOTIPY_CLIENT_SECRET = "d41061364f1b40c681bdf30d5b87d8c8"
SPOTIPY_REDIRECT_URI = "https://localhost:8000/callback"
"""

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])