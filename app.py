import os

from example.demo_ffmpeg import main
import asyncio
from threading import Thread

from flask import Flask, render_template

####################################################################
#                                                                  #
#  SERVIDOR RTMP                                                   #
#                                                                  #
def hls():
    asyncio.run(main())

tHls = Thread(target=hls, args=[])
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################

####################################################################
#                                                                  #
#   SERVIDOR HTTP                                                  #
#                                                                  #
flask = Flask(__name__, static_folder='lives', static_url_path='/streams')


@flask.route('/play/<live>')
def home(live):
    return render_template('player.html', live=live)

@flask.route('/')
def lista():
    arquivos = list(map(lambda arquivo: arquivo.split('.'), os.listdir('lives')))
    lista = []
    for arquivo in arquivos:
        if arquivo[1] == 'm3u8':
            lista.append(arquivo[0])
    return render_template('lista.html', lives=lista)
#                                                                  #
#                                                                  #
#                                                                  #
####################################################################

tHls.start()
flask.run(debug=True)