from message import MESSAGE_BODY
import os
from phone_numbers import TO_NUMBERS
from twilio.rest import Client
from twilio_variables import *


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

from_number = TWILIO_PHONE_NUMBER
message = MESSAGE_BODY


def send(twilio_client, to_number, from_number, message):
    try:
        twilio_client.messages.create(
            to = to_number,
            from_= from_number,
            body = message
        )
    except Exception as e:
        print(e)

def send_to_mutliple_numbers(twilio_client, to_numbers, from_number, message):
    for to_number in to_numbers:
        send(client, to_number, from_number, message)

if __name__ == '__main__':
    send_to_mutliple_numbers(client, TO_NUMBERS, from_number, message)


'''
- response.py
- create receive_sms.py
- add FOI to to_numbers
- upgrade Twilio
''' 

