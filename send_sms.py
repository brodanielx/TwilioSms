import logging
from message import MESSAGE_BODY
import os
from foi import FOI_NUMBERS
from pprint import pformat
from twilio.rest import Client
from twilio_variables import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER

logging.basicConfig(level=logging.WARNING)


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

from_number = TWILIO_PHONE_NUMBER
message = MESSAGE_BODY
to_numbers = FOI_NUMBERS


def send(twilio_client, to_number, from_number, message):
    try:
        message = twilio_client.messages.create(
            to = to_number,
            from_= from_number,
            body = message
        )

        logging.warning(pformat(message.__dict__, indent=2))

    except Exception as e:
        print(e)

def send_to_mutliple_numbers(twilio_client, to_numbers, from_number, message):
    for to_number in to_numbers:
        send(client, to_number, from_number, message)

if __name__ == '__main__':
    send_to_mutliple_numbers(client, to_numbers, from_number, message)


'''
- upgrade Twilio
''' 

