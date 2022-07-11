"""
Gets a deduplicated list of all artists in one or more playlists. 

$env:SPOTIPY_CLIENT_ID='<client id>'
$env:SPOTIPY_CLIENT_SECRET='<client secret>' 
python track_extractor.py <playlist url> <playlist url> ...
"""
import csv
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-library-read"


def get_artists(track):
  return map(lambda artist: artist["name"], track["artists"])


if __name__ == "__main__":
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

  artists = set()

  playlist_urls = sys.argv[2:]
  for url in playlist_urls:
    playlist_items = sp.playlist_items(url)

    for item in playlist_items["items"]:
      track = item["track"]
      for artist in track["artists"]:
        artists.add(artist["name"])

  with open(sys.argv[1], 'w', newline='') as out_file:
    csv_writer = csv.writer(out_file, dialect='excel')
    csv_writer.writerow(["Artist"])

    for artist_name in artists:
      csv_writer.writerow([artist_name])