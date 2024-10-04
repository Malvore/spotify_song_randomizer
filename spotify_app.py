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

# Function to select a random song based on the user’s choice (decade or genre)
def select_random_song_by_decade_or_genre():
    # Present options to the user in a clearer way
    print("How would you like to search for a random song?")
    print("1. By Decade (1940s and onward)")
    print("2. By Genre")

    # Get user input for decade or genre choice
    try:
        choice = int(input("Enter 1 for Decade or 2 for Genre: ").strip())
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
        return

    if choice == 1:
        # Show available decades and choose one
        decades = ['1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020']
        print(f"Available decades: {', '.join([f'{d}s' for d in decades])}")
        
        # Randomly select a decade and a year from that decade
        selected_decade = random.choice(decades)
        year = random.randint(int(selected_decade), int(selected_decade) + 9)
        print(f"Searching for a random track from the {selected_decade}s...")
        result = spotify.search(q=f'year:{year}', type='track', limit=1, offset=random.randint(0, 1000))

    elif choice == 2:
        # Show available genres and choose one
        genres = ['pop', 'rock', 'jazz', 'classical', 'hip-hop', 'country', 'blues', 'reggae', 'electronic', 'metal']
        print(f"Available genres: {', '.join(genres)}")
        
        # Randomly select a genre
        selected_genre = random.choice(genres)
        print(f"Searching for a random {selected_genre} track...")
        result = spotify.search(q=f'genre:"{selected_genre}"', type='track', limit=1, offset=random.randint(0, 1000))

    else:
        print("Invalid choice! Please enter 1 or 2.")
        return

    # Display the selected track if a result is found
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        track_duration = track['duration_ms'] // 1000  # duration in seconds
        track_url = track['external_urls']['spotify']

        # Display song details
        print(f"\nNow Playing: '{track_name}' by {artist_name}")
        print(f"Album: {album_name}")
        print(f"Duration: {track_duration // 60}:{track_duration % 60:02d} minutes")
        print(f"Listen on Spotify: {track_url}")
    else:
        print("No track found. Try again.")

    # Ask if the user wants to randomize again
    retry = input("\nWould you like to search for another random song? (yes/no): ").strip().lower()
    if retry == 'yes':
        select_random_song_by_decade_or_genre()
    else:
        print("Goodbye!")

# Call the function to select and display a random song
select_random_song_by_decade_or_genre()



