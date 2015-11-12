import urllib2
import urllib


base_url = "http://127.0.0.1:5000/song/su.mp3"

if __name__ == "__main__":
    #x = urllib2.urlopen("http://127.0.0.1:5000/song/su.mp3")
    x = urllib.urlretrieve("http://127.0.0.1:5000/song/su.mp3", "mp3.mp3")
    print x.read()