# Spotify Stats

a very simple python script to analyse hours listened by day and most played songs

### How-To

- Request your account data from https://www.spotify.com/us/account/privacy/
- confirm the E-Mail
- up to 30 days later you will get a zip file containing a `MyData` folder containing files similar to those:
  - Follow.json
  - Payments.json
  - Playlist1.json
  - Read_Me_First.pdf
  - SearchQueries.json
  - StreamingHistory0.json
  - StreamingHistory1.json
  - Userdata.json
  - YourLibrary.json
- download the `spotifystats.py` file
- edit the `BASEDIR` path to your `MyData` folder
- run `spotifystats.py`

### Dependencies

- python 3.7 or newer
- matplotlib
