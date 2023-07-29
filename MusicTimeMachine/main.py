from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

ID_CLIENT = "CLIENT ID FROM SPOTIFY"
SECRET = "SECRET FROM SPOTIFY"
URI = "http://example.com"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

# date = input("Insert the year, month and date of your choice (YYYY-MM-DD) > ")

date = "1999-01-27"

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=URL)
billboard = response.text

# Scrapping data from billboard
soup = BeautifulSoup(billboard, "html.parser")

music_name = soup.select("li ul li h3")
artist_name = soup.find_all(name="span", class_="u-max-width-330")

music_list = [music.getText().strip() for music in music_name]
artist_list = [artist.getText().strip() for artist in artist_name]

# Creating playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID_CLIENT,
                                               client_secret=SECRET,
                                               redirect_uri=URI,
                                               scope="playlist-modify-private"))

results = sp.current_user()
user_id = results["id"]

# Searching musics
songs_uri = []
for n in range(0, 100):
    try:
        songs_uri.append(sp.search(q=f"artist:{artist_list[n].split()[0]} track:{music_list[n]}")["tracks"]
        ["items"][0]["uri"])
    except IndexError:
      print(f"Couldn't find this music ({music_list[n]}) by this artist ({artist_list[n].split()[0]})")
        continue

# Creating Playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False,
                                   description='Your spotify playlist based on your date of choice')

playlist_id = playlist["id"]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs_uri, position=None)
