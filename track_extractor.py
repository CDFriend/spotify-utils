"""
Export name and artist for all songs in a playlist to CSV

$env:SPOTIPY_CLIENT_ID='<client id>'
$env:SPOTIPY_CLIENT_SECRET='<client secret>' 
python track_extractor.py <playlist url>
"""
import csv
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-library-read"


def get_artists(track):
  return map(lambda artist: artist["name"], track["artists"])


if __name__ == "__main__":
  playlist_url = sys.argv[2]
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

  playlist_tracks = sp.playlist_items(playlist_url)

  with open(sys.argv[1], 'w', newline='') as out_file:
    csv_writer = csv.writer(out_file, dialect='excel')
    csv_writer.writerow(["Name", "Artists"])

    for item in playlist_tracks["items"][:-1]:
      track = item["track"]
      csv_writer.writerow([track["name"], ", ".join(get_artists(track))])

  print("Wrote output to", sys.argv[1])
    
