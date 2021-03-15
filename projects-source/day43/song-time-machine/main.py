from bs4 import BeautifulSoup as bs
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

print("Welcome to Spotify Time Machine, a fun app to generate playlists for you.")
print("Based on a date you enter, Spotify will create a playlist for you which you can listen to on Spotify app of your choosing.\n\n")
print("Connecting to Spotify.")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
  client_id=CLIENT_ID,
  client_secret=CLIENT_SECRET,
  redirect_uri="http://example.com",
  scope="playlist-modify-private"
))

date = input("Enter a date to view the Bill Board Chart for that time period (YYYY-MM-DD): ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

user_id = sp.current_user()["id"]
playlist_name = f"{date} Billboard 100"

response = requests.get(url)
soup = bs(response.content, 'html.parser')
song_elements = soup.find_all('button', class_='chart-element__wrapper')
song_uris = []
track_list = []
print("Making list of songs on requested date.\n")
for song in song_elements:
  rank = song.find('span', class_='chart-element__rank__number').get_text()
  song_title = song.find('span', class_='chart-element__information__song').get_text()
  results = sp.search(f"track:{song_title}")
  try:
    uri = results["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
    print(f"Could not find {song_title} in Spotify. Skipping for now.")
  artist = song.find('span', class_='chart-element__information__artist').get_text()
  song_str = f"{rank} {song_title} {artist}"
  #print(song_str)
  track_list.append(song_str)

#print(song_uris)

print("Writing track list to file.")
with open("tracklist.txt", 'w') as file:
  for item in track_list:
    file.write(item+"\n")

print(f"Creating the playlist for you for the date {date}")
playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

#sp.user_playlist_add_tracks(user_id, playlist_id, song_uris)
print(f"Success. Playlist created.")