#http://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
from __future__ import unicode_literals
import os, sys
import re
from flask import Flask, request, Response, make_response, send_file
import youtube_dl
#import ssl
#from OpenSSL import SSL


#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')
#ctx.load_cert_chain('ssl.cert', 'ssl.key')

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


def get_song(song_name):
    try:
        src = os.path.join(os.getcwd(), song_name)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route("/song/<song_name>")
def download_song(song_name):
    headers = {"Content-Disposition": "attachment; filename=%s" % song_name}
    return send_file(song_name, mimetype ="Content-Type: audio/mpeg")


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
  #  context = 'adhoc'#('server.crt', 'server.key')
    app.run(debug = True)