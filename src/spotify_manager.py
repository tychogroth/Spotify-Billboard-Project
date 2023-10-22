# Import necessary libraries and modules
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define a class named SpotifyManager
class SpotifyManager:
    # The constructor method which gets called when a new object of SpotifyManager is created
    def __init__(self):
        # Create a Spotify client instance with authorization using environment variables
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="playlist-modify-public playlist-modify-private"
        ))
        # Get and store the user's Spotify ID
        self.user_id = self.sp.me()['id']

    # Method to get Spotify URIs for each song in the chart data
    def get_spotify_uris(self, chart_data):
        # Initialize an empty list to store Spotify URIs
        spotify_uris = []
        # Iterate through each song in the chart data
        for song_data in chart_data:
            # Construct the search query using the song title and artist name
            query = f"track:{song_data['title']} artist:{song_data['artist']}"
            try:
                # Search Spotify for the song using the query
                result = self.sp.search(q=query, type="track", limit=1)
                # Get the first track from the search results
                track = result['tracks']['items'][0]
                # Append the Spotify URI of the track to the spotify_uris list
                spotify_uris.append(track['uri'])
            except IndexError:
                # If no track is found (i.e., the search results are empty), continue to the next song
                continue
        # Return the list of Spotify URIs
        return spotify_uris

    # Method to create a new Spotify playlist
    def create_playlist(self, date):
        # Construct the playlist name using the given date
        playlist_name = f"{date} Billboard 100"
        # Create a new private Spotify playlist with the constructed name
        playlist = self.sp.user_playlist_create(self.user_id, playlist_name, public=False)
        # Return the Spotify ID of the newly created playlist
        return playlist['id']

    # Method to add songs to the specified Spotify playlist
    def add_songs_to_playlist(self, playlist_id, spotify_uris):
        # Split the list of Spotify URIs into chunks of 100 URIs each (as Spotify's limit is 100 URIs per request)
        uri_chunks = [spotify_uris[i:i + 100] for i in range(0, len(spotify_uris), 100)]
        # Iterate through each chunk of URIs
        for chunk in uri_chunks:
            # Add the chunk of URIs to the specified Spotify playlist
            self.sp.playlist_add_items(playlist_id, chunk)
