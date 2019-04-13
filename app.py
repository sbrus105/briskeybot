import os
import sys
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  if data['name'] != 'briskeybot':
  
    if 'Frost' or 'frost' in data['text']:
		msg = 'Fuck John Frost!'
	else
		return "ok", 200
		
	send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  
	#5d108f5841a9977ddfa018e014  	The Deuce
	#44730fb274b2b3538d071f6f84		Tester
  data = {
          'bot_id' : '44730fb274b2b3538d071f6f84',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
