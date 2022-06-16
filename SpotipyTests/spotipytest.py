from os import name
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyClientCredentials
import yaml

# Import client info
with open('client_info.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
print('data: ', data)
client_id = data['client_id']
client_secret = data['client_secret']
# client_redirect_url = 'https://accounts.spotify.com/api/token'
client_redirect_url = 'http://example.com'

# the following line doesn't work because it is for non-logged in users only
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

client_scope = "user-read-currently-playing, user-read-playback-state, user-modify-playback-state, playlist-modify-public, playlist-modify-private, playlist-read-private, playlist-read-collaborative"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_redirect_url, scope=client_scope))


# sp.start_playback()
# sp.pause_playback()

print('Crtl+C to exit.')
while True:

    command = input('>_ ')

    if command == 'play':
        playback_info = sp.current_playback()
        is_playing = playback_info['is_playing']
        if not is_playing:
            sp.start_playback()
        else:
            print('already playing')

    elif command == 'pause':
        playback_info = sp.current_playback()
        is_playing = playback_info['is_playing']
        if is_playing:
            sp.pause_playback()
        else:
            print('already paused')
    elif command == 'next':
        sp.next_track()
    elif command == 'prev':
        sp.previous_track()
    elif command == 'add':
        current_song = sp.currently_playing()
        current_playlist = sp.current_playback()['context']['uri']
        print(current_playlist)
        playlist_items = sp.playlist_items(current_playlist)
        # print(playlist_items)
        for entry in playlist_items['items']:
            print(entry['track']['name'])
         
        sp.playlist_add_items(current_playlist, current_song)

        

