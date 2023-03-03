from tidal_dl import Tidal

# Create an instance of the Tidal class
tidal = Tidal()

# Login to Tidal
tidal.login('ashaikh2@email.davenport.edu', 'Login20000')

# Search for a track
search_results = tidal.search('Bam')
track_id = search_results['tracks']['items'][0]['id']

# Download the track
tidal.download_track(track_id)
