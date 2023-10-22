# Import the BillboardScraper class from the billboard_scraper module
from src.billboard_scraper import BillboardScraper
# Import the SpotifyManager class from the spotify_manager module
from src.spotify_manager import SpotifyManager

# Define a class named PlaylistCreator
class PlaylistCreator:
    # The constructor method which gets called when a new object of PlaylistCreator is created
    def __init__(self, date):
        self.date = date  # Store the date input as an instance variable
        # Create an instance of BillboardScraper with the specified date
        self.billboard_scraper = BillboardScraper(date)
        # Create an instance of SpotifyManager
        self.spotify_manager = SpotifyManager()

    # Method to orchestrate the process of creating a billboard playlist on Spotify
    def create_billboard_playlist(self):
        # Get the chart data from the billboard_scraper instance
        chart_data = self.billboard_scraper.chart_data
        # Get the Spotify URIs for the songs in the chart data using spotify_manager instance
        spotify_uris = self.spotify_manager.get_spotify_uris(chart_data)
        # Create a new Spotify playlist using spotify_manager instance and store the playlist ID
        playlist_id = self.spotify_manager.create_playlist(self.date)
        # Add the songs to the newly created playlist using spotify_manager instance
        self.spotify_manager.add_songs_to_playlist(playlist_id, spotify_uris)
