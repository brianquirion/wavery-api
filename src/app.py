import json
import os
import sys
from flask import Flask, request, jsonify
from src.service.mail import send_mail

sys.path.insert(0, os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi!!'

@app.route('/mail', methods=['POST'])
def mail():
    if 'full_name' not in request.json or 'sender' not in request.json \
        or 'subject' not in request.json \
        or 'message' not in request.json:
        return jsonify(message='Missing arguments in payload'), 400

    with open('src/config.json') as f:
        config = json.load(f)

    body = request.json
    email_message = '<h3>Message envoyé depuis le formulaire de contact.</h3><br/>'
    email_message += '<strong>Nom du destinataire : </strong>{}<br/>'.format(body['full_name'])
    email_message += '<strong>Courriel : </strong>{}<br/>'.format(body['sender'])
    email_message += '<strong>Sujet : {}</strong><br/>'.format(body['subject'])
    email_message += '<strong>Message : {}</strong><br/><br/>'.format(body['message'])

    try:
        send_mail(config['mail_from'], config['mail_to'], body['sender'], body['subject'], body['message'])
    except Exception as e:
        print(e.args)
        return jsonify(message=e.args[1]), 400
    return '', 200
