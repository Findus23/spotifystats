import json
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt

# minumum time a song needs to be played to count as "played"
MIN_PLAY_TIME = 60  # seconds

# only show songs that were played at least this often in the top list
MIN_PLAY_NUM = 3

# path to Spotify export
BASEDIR = Path("/home/lukas/Nextcloud/MyData/")


@dataclass
class Song:
    end_time: str
    artist_name: str
    track_name: str
    ms_played: int

    def datetime(self) -> datetime:
        return datetime.strptime(self.end_time, "%Y-%m-%d %H:%M")

    def date(self):
        return self.datetime().date()

    @property
    def min_played(self) -> float:
        return self.ms_played / 1000 / 60


history = []

for file in BASEDIR.glob("StreamingHistory*.json"):
    with file.open() as f:
        data = json.load(f)
    for song in data:
        try:
            song_obj = Song(end_time=song["endTime"], artist_name=song["artistName"],
                            track_name=song["trackName"], ms_played=song["msPlayed"])
            history.append(song_obj)
        except KeyError:
            print("this entry doesn't seem to be a song")
            continue

print(f"{len(history)} plays found")

bins = {}
for song in history:
    if song.date() in bins:
        bins[song.date()] += song.min_played
    else:
        bins[song.date()] = song.min_played

plt.bar(bins.keys(), bins.values())
plt.ylabel("minutes")

played_songs = []
for song in history:
    if song.ms_played > MIN_PLAY_TIME * 1000:
        played_songs.append((song.artist_name, song.track_name))

for (artist, title), num_played in sorted(Counter(played_songs).most_common(), key=lambda c: [-c[1], c[0][0], c[0][1]]):
    if num_played >= MIN_PLAY_NUM:
        print(f"{num_played:>4} {artist}: {title}")

plt.show()
