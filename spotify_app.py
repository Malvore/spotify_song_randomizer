import spotipy  
from spotipy.oauth2 import SpotifyOAuth  
  
# Step 1: Define your API credentials and redirect URI
client_id = "56a3c8c6668247c48bf88e5c6f31bfc7"
client_secret = "9f6cb8d1d303445495f6ac21ddea3896"
redirect_uri = "http://localhost:8888/callback"  # Make sure this matches what you set in the Spotify dashboard

# Step 2: Create a SpotifyOAuth object
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope="user-library-read")  # Adjust scope based on the access you need

# Step 3: Get the access token and refresh token
token_info = sp_oauth.get_access_token(as_dict=False)

# Step 4: Extract the access token
access_token = token_info['access_token']

# Step 5: Use the access token to interact with the Spotify API
spotify = spotipy.Spotify(auth=access_token)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])