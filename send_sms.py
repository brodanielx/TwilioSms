import os
from to_numbers import *
from twilio.rest import Client
from twilio_variables import *


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

from_number = TWILIO_PHONE_NUMBER

url = "http://noitampa.org/"
message = "Peace! This is a test message.\n" + url


def send_message(twilio_client, to_number, from_number, message):
    try:
        twilio_client.messages.create(
            to = to_number,
            from_= from_number,
            body = message
        )
    except Exception as e:
        print(e)

for to_number in TO_NUMBERS:
    send_message(client, to_number, from_number, message)


'''
- add if __name to run
- create message.py, response.py
- create receive_sms.py
- add FOI to to_numbers
- upgrade Twilio
''' 

