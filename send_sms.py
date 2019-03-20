import datetime
from sms_logger import create_file_path, create_logger, format_twilio_message_instance
from message import MESSAGE_BODY
import os
from foi import FOI_NUMBERS
from pprint import pformat
from twilio.rest import Client
from twilio_variables import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE_NUMBER

file_path = create_file_path('sms_send')
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

        log_string = format_twilio_message_instance(messageInstance)
        logger.info(log_string)
    
    except Exception as e:
        print(e)

def send_to_mutliple_numbers(twilio_client, to_numbers, from_number, message):
    for to_number in to_numbers:
        send(client, to_number, from_number, message)

def send_in_segments(twilio_client, to_numbers, from_number, message):
    segments = segmentize(message)
    for segment in segments:
        send_to_mutliple_numbers(twilio_client, to_numbers, from_number, segment)
        print(f'--------\n{segment}\n')

def segmentize(message, segment_length = 150):
    message_length = len(message)
    segments = [ message[i:i+segment_length] for i in range(0, message_length, segment_length) ] 
    segment_count = len(segments)
    segment_count_str = str(segment_count)
    return [ f'({str(i+1)}/{segment_count_str}) {segments[i]}' for i in range(len(segments)) ]


if __name__ == '__main__':
    send_in_segments(client, to_numbers, from_number, message)

