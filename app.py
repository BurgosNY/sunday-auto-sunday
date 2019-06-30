from pytube import YouTube
from flask import Flask, request, render_template
import settings


app = Flask(__name__)


yt = YouTube('https://www.youtube.com/watch?v=LnmROydlJn0&t=3s')
c = yt.captions.get_by_language_code('pt').generate_srt_captions()


@app.route("/")
def home():
    legends = [x for x in c.split('\n')]
    return render_template('index.html', legends=legends)
