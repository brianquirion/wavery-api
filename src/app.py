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
    if 'full_name' not in request.args 
        or 'sender' not in request.args 
        or 'subject' not in request.args
        or 'message' not in request.args:
        return jsonify(message='Missing arguments in payload', status=400, category='error')

    with open('src/config.json') as f:
        config = json.load(f)

    body = request.json
    email_message = '<h3>Message envoyé depuis le formulaire de contact.</h3><br/>'
    email_message += '<strong>Nom du destinataire : </strong>{}<br/>'.format(body['full_name'])
    email_message += '<strong>Courriel : </strong>{}<br/>'.format(body['sender'])
    email_message += '<strong>Sujet : {}</strong><br/>'.format(body['subject'])
    email_message += '<strong>Message : {}</strong><br/><br/>'.format(body['message'])

    try:
        send_mail(config['mail_from'], config['mail_to'], body['sender'], subject, body)
    except Exception as e:
        return jsonify(message=e.args[1], status=400, category='error')
    return jsonify(status=200, category='success')
