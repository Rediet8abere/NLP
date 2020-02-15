# from google.cloud import translate_v2
"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""

# from google.cloud import translate_v2 as translate
# export GOOGLE_APPLICATION_CREDENTIALS = "credentials.json"
from google.cloud import translate_v2 as translate
from flask import Flask
import os
import six
import requests
import json

API_KEY = 'trnsl.1.1.20200215T092345Z.92ff7209205a701f.cae85a5006bdbe8ff9ac5ec0b50a40ddee011936'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = dict(key=API_KEY, text='hello', lang='en-es')
res = requests.get(url, params)
print("res", res.text)
