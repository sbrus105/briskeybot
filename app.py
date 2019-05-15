import os
import sys
import json
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__) #dont touch
gbq = "GBQ"
frost = "Frost"
@app.route('/', methods=['POST'])


def webhook():
  data = request.get_json()
  log('Received {}'.format(data))

  if data['name'] != 'briskeybot':  #not message from self
    if random.randint(1, 101) == 42:
        msg = "Shut the fuck up, @" + data['name']
        send_message(msg)
        return "ok", 200
    if re.search('gbq', data['text'], re.IGNORECASE):
        msg = "It's Jacob."
        send_message(msg)
    if re.search('frost', data['text'], re.IGNORECASE):
        msg = "Fuck Jonathan Frost!"
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
