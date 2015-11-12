#http://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
from __future__ import unicode_literals
import os, sys
import re
from flask import Flask, request, Response, make_response, send_file
import youtube_dl

app = Flask(__name__)
app.config.from_object(__name__)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192', 
    }], 
}

dest_path = "/Users/ilyssa/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized"

@app.route("/downloadsong/<song_name>")
def download_song(song_name):
    return send_file(song_name, mimetype ="Content-Type: audio/mpeg")

@app.route("/listsongs")
def list_songs():
    path = os.getcwd()
    dirs = os.listdir(path)
    return "\n".join(file for file in dirs if file.endswith(".mp3"))

@app.route("/grabsong", methods=['POST', 'GET'])
def grab_song():
    error = None
    if request.method == 'POST':
        link = request.form["link"]
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return "Success"
    else:
        return '''
            <form action="" method="post">
                <p><input type=text name=link>
                <p><input type=submit value=grabsong>
            </form>
            '''


if __name__ == "__main__":
    app.run(debug = True)