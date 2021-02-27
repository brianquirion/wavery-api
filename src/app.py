import json
import os
import sys
from flask import Flask
from src.service.mail import send_mail

sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi!!'

@app.route('/mail')
def mail():
    with open('src/config.json') as f:
        config = json.load(f)
    return send_mail(config['mail_from'], config['mail_to'])
