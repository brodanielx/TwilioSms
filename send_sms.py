import datetime
from get_logger import create_file_path, create_logger
from message import MESSAGE_BODY
import os
from foi import FOI_NUMBERS
from pprint import pformat
from twilio.rest import Client
from twilio_variables import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER


# today_string = datetime.datetime.today().strftime('_%m%d%y')
# file_name = f'sms{today_string}.log'
# file_path = os.path.join('logs', file_name)

file_path = create_file_path()
logger = create_logger(file_path=file_path)


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

from_number = TWILIO_PHONE_NUMBER
message = MESSAGE_BODY
to_numbers = FOI_NUMBERS


def send(twilio_client, to_number, from_number, message):
    try:
        messageInstance = twilio_client.messages.create(
            to = to_number,
            from_= from_number,
            body = message
        )

        logger.info(pformat(messageInstance.__dict__['_properties'], indent=2))

    except Exception as e:
        print(e)

def send_to_mutliple_numbers(twilio_client, to_numbers, from_number, message):
    for to_number in to_numbers:
        send(client, to_number, from_number, message)

if __name__ == '__main__':
    send_to_mutliple_numbers(client, to_numbers, from_number, message)

