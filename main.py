import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import json

client_credentials_manager = SpotifyClientCredentials(client_id=None, client_secret=None)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

scope = 'playlist-modify-public'
username = '12169442849'
playlist_ids = ['7lvkaNHordUe3PZHDzoPWK',
                '77yfHG2KJmGM56U8B3a4cw']

token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

def get_all_tracks_from_playlist(playlist_id):
    tracks_response = sp.playlist_tracks(playlist_id)
    tracks = tracks_response["items"]
    while tracks_response["next"]:
        tracks_response = sp.next(tracks_response)
        tracks.extend(tracks_response["items"])
    return tracks

#for playlist_id in playlist_ids:
songs = get_all_tracks_from_playlist('7lvkaNHordUe3PZHDzoPWK') + get_all_tracks_from_playlist('77yfHG2KJmGM56U8B3a4cw')

links = []
for song in songs:
    link = song['track']['uri']
    links.append(link)

duplicates = set([x for x in links if links.count(x) > 1])
print(duplicates)

#create new playlist
spotifyObject.user_playlist_create(user=username,name='Duplicates',public=True,description=None)

#find the new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#add songs
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=duplicates)

#playlists 1 and 2
#playlist1 = spotifyObject.user_playlist(user=username,playlist_id=playlist1, fields=, market=None)
#playlist2 = spotifyObject.user_playlist(user=username, playlist_id=playlist2, fields=None, market=None)





'''
#create the playlist
playlist_name = input("Enter a playlist name:")
playlist_description = input("Enter a playlist description:")

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_description)

user_input = input('Enter a song:')
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    #print(json.dumps(result,sort_keys=4,indent=4)
    list_of_songs.append((result['tracks']['items'][0]['uri']))
    user_input = input('Enter a song:')

#find the new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#add songs
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist, tracks=list_of_songs)'''


