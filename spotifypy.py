import spotipy
import var
from spotipy.oauth2 import SpotifyClientCredentials


auth_manager = SpotifyClientCredentials(
        client_id=var.client_id,
        client_secret=var.client_secret
    )

spotify = spotipy.Spotify(auth_manager=auth_manager)
results = spotify.playlist(var.playlist_uri)


counter = 1
for track in spotify.playlist_tracks(var.playlist_uri)["items"]:
    track_artist = track["track"]["artists"][0]["name"]
    album_name = track["track"]["album"]["name"]
    track_name = track["track"]["name"]
    track_uri = track["track"]["uri"]

    print("{}: {} - {} - {}\n\t{}\n\tAudio features: {}\n".format(counter, track_artist, album_name, track_name, track_uri, spotify.audio_features(track_uri)[0]))
    counter += 1
