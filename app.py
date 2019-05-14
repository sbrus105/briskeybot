import os
import sys
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__) #dont touch

@app.route('/', methods=['POST'])


def webhook():
  data = request.get_json()
  log('Received {}'.format(data))

  if data['name'] != 'briskeybot':  #not message from self
    if "GBQ" in data['text']:
        msg = "It's Jacob."
        send_message(msg)
    if "Gbq" in data['text']:
        msg = "It's Jacob."
        send_message(msg)
    elif "gbq" in data['text']:
        msg = "It's Jacob."
        send_message(msg)
    elif "Frost" in data['text']:
        msg = "Fuck John Frost!"
        send_message(msg)
    elif "frost" in data['text']:
        msg = "Fuck John Frost!"
        send_message(msg)
  return "ok", 200


def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  
#5d108f5841a9977ddfa018e014  	The Deuce
#44730fb274b2b3538d071f6f84		Tester
  data = {
          'bot_id' : '5d108f5841a9977ddfa018e014',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()


def log(msg):
  print(str(msg))
  sys.stdout.flush()
