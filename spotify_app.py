import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import random
import datetime

#set current date and time
today = datetime.date.today()
current_year = today.year

#uncomment below to print the current year
#print(current_year)

#Load environment variables from .env file
load_dotenv("/home/aaron/local-python-files/spotify_song_randomizer/spotify.env")

# Create a SpotifyOAuth object and authenticate
sp_oauth = SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                        scope="user-library-read")

#Get the access token
access_token = sp_oauth.get_access_token(as_dict=False)

# Use the access token to create a Spotify API client
spotify = spotipy.Spotify(auth=access_token)

# Function to select a random song based on the user’s choice (decade or genre)
def select_random_song_by_decade_or_genre():
    while True:
        # Present options to the user in a clearer way
        print("How would you like to search for a random song?")
        print("1. By Year")
        print("2. By Genre")

        #Avoid unbound error by setting result variable to None.
        result = None  
        
        #Get user input, and use exit to quit the application.
        try:
            choice_input = input("Enter 1 for year or 2 for genre: ").strip()
            if choice_input.lower() == "exit":
                print("Goodbye!")
                break
            
            choice = int(choice_input)
        except ValueError:
            print("Invalid input! Please enter a number (1 or 2).")
            continue 

        if choice == 1:
            # Show available years and choose one
            available_years = range(1940,current_year + 1)
            print(f"Available years: {min(available_years)} to present ")

            #Get year input from user, offer the ability to exit.
            year_input = input("Choose a year: ")
            if year_input.lower() == "exit":
                print("Goodbye!")
                break

            #convert to an integer
            try:
                selected_year = int(year_input)

                if selected_year not in available_years:
                    print(f"Please enter a valid year between {available_years} and now ")    

                else:
                    print(f"Searching for a random track from {selected_year}...")
                    result = spotify.search(q=f'year:{selected_year}', type='track', limit=1, offset=random.randint(0, 50))

            except ValueError:
                print("Invalid input. Please enter a valid year.")


        elif choice == 2:
            # Show available genres and choose one
            genres = [
                    'pop', 'funk', 'alternative', 'dance', 'rock', 'jazz', 'classical', 
                    'hip-hop', 'country', 'blues', 'reggae', 'electronic', 'metal']
            print(f"Available genres: {', '.join(genres)}")
        
            #Get genre input from user, offer the ability to exit.
            genre_input = input("Choose from the available genres: ")
            if genre_input.lower() == "exit":
                print("Goodbye!")
                break

            #convert to a string
            try:
                selected_genre = str(genre_input)

                if selected_genre not in genres:
                    print("Please enter an available genre from the list")

                else:
                    # Randomly select a genre
                    print(f"Searching for a random {selected_genre} track...")
                    result = spotify.search(q=f'genre:"{selected_genre}"', type='track', limit=1, offset=random.randint(0, 50))

            except ValueError:
                print("Invalid input. Please enter a valid genre")

        else:
            print("Invalid choice! Please enter 1 or 2.")
            continue

        # Display the selected track if a result is found
        if result and 'tracks' in result and result['tracks']['items']:
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
            print("No track found or invalid response. Try again.")

        # Ask if the user wants to randomize again
        retry = input("\nWould you like to search for another random song? (yes/no): ").strip().lower()
        if retry == 'no' or retry == "exit":
            print("Goodbye!")
            break
        

# Call the function to select and display a random song
select_random_song_by_decade_or_genre()



