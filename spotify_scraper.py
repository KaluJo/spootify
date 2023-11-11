import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

# Set up your credentials, you can get these from the Spotify Developer Dashboard after you authenticate
client_id = '###'
client_secret = '###'

# Initialize
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# List of playlist URLs
playlist_urls = [
  # ADD YOUR PLAYLIST'S URL HERE! YOU CAN INCLUDE THE FULL URL OR JUST THE ID
]

file_counter = 1

# Process each playlist URL
for playlist_url in playlist_urls:
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist(playlist_id)

    playlist_data = {
        'cover_image': results['images'][0]['url'],
        'name': results['name'],
        'description': results['description'],
        'tracks': []
    }

    for track in results['tracks']['items']:
        song = track['track']
        track_data = {
            'song_cover_image': song['album']['images'][0]['url'],
            'song_title': song['name'],
            'artist': ', '.join(artist['name'] for artist in song['artists']),
            'album': song['album']['name'],
            'song_clip': song.get('preview_url'),
            'impressions': '',
            'discovery': '',
            'notes': ''
        }

        playlist_data['tracks'].append(track_data)

    # Convert playlist data to JSON
    playlist_json = json.dumps(playlist_data, indent=4)

    # Create a numbered file for each playlist
    file_name = f'playlist_data_{file_counter}.json'
    with open(file_name, 'w') as json_file:
        json_file.write(playlist_json)

    print(f'Playlist data has been saved to {file_name}')
    
    # Let's go again
    file_counter += 1