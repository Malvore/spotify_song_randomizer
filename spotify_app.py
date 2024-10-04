import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv("/home/aaron/spotify_randomizer_app/spotify.env")

# Create a SpotifyOAuth object and authenticate
sp_oauth = SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                        scope="user-library-read")

# Get the access token
access_token = sp_oauth.get_access_token(as_dict=False)

# Use the access token to create a Spotify API client
spotify = spotipy.Spotify(auth=access_token)

# Function to select a random song
def select_random_song():
    year = random.randint(2000, 2023)  # Random year
    result = spotify.search(q=f'year:{year}', type='track', limit=1, offset=random.randint(0, 1000))
    
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        print(f"Playing '{track['name']}' by {track['artists'][0]['name']}")
        print(f"Listen on Spotify: {track['external_urls']['spotify']}")
    else:
        print("No track found. Try again.")

# Call the function to select and display a random song
select_random_song()
