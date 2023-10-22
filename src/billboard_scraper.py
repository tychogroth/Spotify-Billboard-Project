# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Define a class named BillboardScraper
class BillboardScraper:
    # A constant to hold the base URL of the Billboard charts
    BASE_URL = 'https://www.billboard.com/charts/hot-100/'

    # The constructor method which gets called when a new object of BillboardScraper is created
    def __init__(self, date):
        self.date = date  # Store the date passed as an argument
        self.chart_data = self.scrape_data()  # Call the scrape_data method to get chart data

    # Method to scrape the Billboard chart data
    def scrape_data(self):
        # Send an HTTP GET request to the Billboard chart URL for the specified date
        response = requests.get(f"{self.BASE_URL}{self.date}")
        # Check the response status and raise an exception for bad requests
        response.raise_for_status()
        # Store the HTML content of the page
        billboard_html = response.text
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(billboard_html, 'html.parser')
        # Select the song title elements using CSS selectors
        songs = soup.select(".chart-results-list li h3")
        # Select the artist name elements using CSS selectors
        artists = soup.select(".chart-results-list li span.c-label.a-no-trucate.a-font-primary-s")
        # Create a list of dictionaries to hold the title and artist for each song
        # This is done by iterating through the songs and artists lists in tandem using zip
        chart_data = [{"title": song.text.strip(), "artist": artist.text.strip()} for song, artist in zip(songs, artists)]
        # Return the chart data list
        return chart_data
