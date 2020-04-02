import os
import sys
import json
import re
import random
import time

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__) #dont touch
@app.route('/', methods=['POST'])


def webhook():
  data = request.get_json()
  log('Received {}'.format(data))
#---------------------------------------------------------
  if data['name'] != 'briskeybot':                       #not message from self
    if random.randint(0,501) == 42:
        msg = "Shut the fuck up."
        send_message(msg)
    if re.search('gbq', data['text'], re.IGNORECASE):    #It's Jacob If                #The meat
        msg = "It's Jacob."
        send_message(msg)
    if re.search('frost', data['text'], re.IGNORECASE):  #Frost if
        msg = "Fuck Jonathan Frost!"
        send_message(msg)
    if re.search('nigger', data['text'], re.IGNORECASE):  #Nig if
        msg = "Whoa there, @" + data['name'] + "! That's pretty offensive, please use the correct terminology, 'Basketball American'!"
        send_message(msg)
    if re.search('nigga', data['text'], re.IGNORECASE):  #Niga if
        msg = "Whoa there, @" + data['name'] + "! That's pretty offensive, please use the correct terminology, 'Basketball American'!"
        send_message(msg)
    if re.search('chad', data['text'], re.IGNORECASE):  #Chad if
        if randTen() > 59:
            msg = "You know who's a damn chad? @Caleb Sims, that's who."
            send_message(msg)
    if re.search('everclear', data['text'], re.IGNORECASE):  #everclear if
        if randTen() > 59:
            msg = "Nothing good ever came out of a night that started with Everclear, remember that."
            send_message(msg)
    if re.search('no homo', data['text'], re.IGNORECASE):  #homo if
        if randTen() > 59:
            msg = "yes homo"
            send_message(msg)
    if re.search('dick cheese', data['text'], re.IGNORECASE):  #cheese if
        msg = "@Jacob Gonzales @Josh Rothfus"
        send_message(msg)
    if re.search(' 69 ', data['text'], re.IGNORECASE):  #everclear if
        if randTen() > 59:
            msg = "Nice."
            send_message(msg)
    if re.search('gamer', data['text'], re.IGNORECASE):  #everclear if
        if randTen() > 59:
            msg = "Gamer's are the most oppressed minority."
            send_message(msg)
    if re.search(' 420 ', data['text'], re.IGNORECASE):  #everclear if
        if randTen() > 59:
            msg = "Blaze it"
            send_message(msg)
    if re.search('born on a beach', data['text'], re.IGNORECASE):  #chant if
        msg = "RAISED IN A CAVE!"
        send_message(msg)
    if re.search('fucking and fighting is all i crave', data['text'], re.IGNORECASE):  #chant if
        msg = "SWEET-MEAT HUNG LIKE A RAILROAD TIE!"
        send_message(msg)
    if re.search("I'm a bad motherfucker", data['text'], re.IGNORECASE):  #chant if
        msg = "I'M A SIGMA PI!"
        send_message(msg)
  return "ok", 200  #send all applicable messages
#---------------------------------------------------------
def randHund():
    int = random.randint(0,101)
    return int

def send_message(msg):

    from time import sleep
    sleep(0.2)

    url  = 'https://api.groupme.com/v3/bots/post'
  
    #5d108f5841a9977ddfa018e014  	The Deuce
    #44730fb274b2b3538d071f6f84		Tester
    data = {
        'bot_id' : '5d108f5841a9977ddfa018e014', #replace this code with above ones for corresponding GM
        'text'   : msg,
       }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def log(msg):
  print(str(msg))
  sys.stdout.flush()
