# Import the PlaylistCreator class from the src.playlist_creator module
from src.playlist_creator import PlaylistCreator

# The __name__ variable is a special built-in variable in Python.
# When a script is run directly, __name__ is set to "__main__". 
# This block of code will only run if the script is run directly, not if it's imported as a module.
if __name__ == "__main__":
    # Prompt the user to enter a date and store the input in the variable date
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
    # Create an instance of the PlaylistCreator class, passing the date as an argument
    playlist_creator = PlaylistCreator(date)
    # Call the create_billboard_playlist method on the playlist_creator object to create the playlist
    playlist_creator.create_billboard_playlist()
    # Print a success message to the console
    print("Playlist created!")

# This script acts as the entry point of your program.
# It creates an instance of the PlaylistCreator class and calls a method on it to create a playlist.
# A success message is printed to the console once the playlist is created.
