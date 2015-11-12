import os
import shutil
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
    if not os.path.exists('songs.txt'):
        open('songs.txt', 'w').close()
    song_names = diff_songs(list_songs())
    path = os.getcwd()
    if not os.access(path + '/Songs/', os.F_OK):
        os.mkdir(path+'/Songs/')
    with open('songs.txt', 'a') as song_file:
        os.chdir(path+'/Songs/')    
        for song_name in song_names:
            download_song(song_name)
            print song_name
            song_file.write(song_name+'\n')
    shutil.move(path+'/Songs/', dest_path)

def diff_songs(server_songs):
    with open('songs.txt') as song_file:
        client_songs = set(song_name.rstrip() for song_name in song_file)
    server_songs = set(server_songs)
    return server_songs - client_songs

if __name__ == "__main__":
    get_all_songs()