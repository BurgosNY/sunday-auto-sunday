import flask
from pytube import YouTube


app = flask.Flask(__name__)


@app.route('/')
def home():
    return 'Olá Gente!'


@app.route('/legendas/<url_video>')
def legenda(url_video):
    return criar_legenda(url_video)


def criar_legenda(codigo_video):
    link_video = f'https://www.youtube.com/watch?v={codigo_video}'
    yt = YouTube(link_video)
    legenda = yt.captions.get_by_language_code('pt')
    return legenda.xml_captions
