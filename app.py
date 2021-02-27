import json
import os
import sys
from flask import Flask

sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi!!'

@app.route('/mail')
def mail():
    with open('config.json') as f:
        config = json.load(f)
    return config['test_secret']
