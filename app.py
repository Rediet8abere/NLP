# from google.cloud import translate_v2
"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""

# from google.cloud import translate_v2 as translate
# export GOOGLE_APPLICATION_CREDENTIALS = "credentials.json"
# from google.cloud import translate_v2 as translate
from flask import Flask,render_template, url_for, jsonify, request, redirect
from gtts import gTTS
import speech_recognition as sr
import pyaudio
import os
# import six
import requests
import json
from pymongo import MongoClient

client = MongoClient()
db = client.TranslateL
LangMp3 = db.LangToAudio
Lang = db.LangToLang

API_KEY = 'trnsl.1.1.20200215T092345Z.92ff7209205a701f.cae85a5006bdbe8ff9ac5ec0b50a40ddee011936'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=["GET", "POST"])
def translate():
    # return render_template('get_voice.html')
    # Speech to text

    r = sr.Recognizer()
    with sr.Microphone() as source:

        # print("say something")
        # audio = r.listen(source)
        if request.method == "POST":
             data = {}    #// empty dict to store data
             content = request.get_json(force=True)
             print("content", content)

             try:
                 text = content['text']
                 print("text", text)
                 # text_list = text.split()
                 # print("text_list", text_list)
                 # print('eng', text_list[0])
                 # print('span', text_list[2])
                 # translation
                 params1 = dict(key=API_KEY, text=text, lang='en-es')
                 # params2 = dict(key=API_KEY, text='hola ¿cómo estás', lang='es-en')
                 # res2 = requests.get(url, params2)
                 # print("res", res2.text)
                 res1 = requests.get(url, params1)
                 d = eval(res1.text)
                 print("hola", d['text'])
                 print("d type", type(d['text'][0]))
                 # text to speech
                 sample = d['text'][0]
                 Lang.insert_one(sample)
                 print("sample", sample)
                 output = gTTS(text=sample, lang='es', slow=False)
                 print("output", output)
                 LangMp3.insert_one(output.save('output.mp3'))
                 # return render_template('audio.html', audios=Lang.find() )
                 # print("voice", voice)
                 # print("sample", sample)
                 # return render_template('index.html')
                 # return redirect(url_for('audio'))
             except:
                 print("voice not clear")

@app.route('/features')
def features():
    return render_template('features.html')


# @app.route('/audio')
# def audio():
#     """Show all playlists."""
#     print("in here")
#     return render_template('audio.html', audios=Lang.find() )





if __name__ == '__main__':
    app.run(debug=True)







# os.system('start output.mp3')
# print("header", res.headers)
