#http://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
from __future__ import unicode_literals
import os, sys
import re
from flask import Flask, request
import youtube_dl
from OpenSSL import SSL


context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

app = Flask(__name__)

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192', 
    }], 
}

@app.route("/")
def hello():
    path = os.getcwd()
    dirs = os.listdir( path )
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
    app.debug = True
    app.run(ssl_context='adhoc')