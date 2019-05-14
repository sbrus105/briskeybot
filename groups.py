import re

def list_to_message(list):
    for name in list:
        msg = '{} @{}'.format(msg, name)
    return msg

def process_groups(msg):
    mentions = re.findall(r'\B@\w+', msg['text'])   # Find all words in msg starting with @
    for group in mentions:
        if group in known_groups:
            to_names = list_to_message(known_groups[group])
            msg_out = '{} {} wants something from you'.format(msg, from_name)
            send_message(msg_out)
