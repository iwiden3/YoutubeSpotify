import urllib2
import urllib

dest_path = "/Users/ilyssa/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized"
base_url = "http://127.0.0.1:5000"

def download_song(song_name):
	urllib.urlretrieve(base_url+"/downloadsong/"+song_name, song_name)

def clean_song_name(song_name):
	return song_name[:song_name.index('(')]

def list_songs():
	response = urllib2.urlopen(base_url+"/listsongs")
	html = response.read()
	return html.split('\n')

def get_all_songs():
	song_names = list_songs()
	for song_name in song_names:
		download_song(song_name)

if __name__ == "__main__":
	get_all_songs()