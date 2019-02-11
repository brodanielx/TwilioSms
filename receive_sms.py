import os
from flask import Flask, request, redirect
from foi import FOI
from person import get_person_by_phone_number
from pprint import pprint
from response import get_personalized_response
from send_sms import send
from sms_logger import (
    create_file_path, create_logger, 
    format_incoming_sms_request, format_twilio_message_instance,
)
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio_variables import *

file_path = create_file_path('sms_send')
logger = create_logger(file_path=file_path)


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

people = FOI

admin_number = ADMIN_NUMBER
twilio_number = TWILIO_PHONE_NUMBER

app = Flask(__name__)

def forward_message(twilio_client, to_number, twilio_number, twilio_request):

    # format_incoming_sms_request(twilio_request)
    log_string = format_incoming_sms_request(twilio_request)
    logger.info(log_string)

    from_number = twilio_request.values.get('From', None)
    body = twilio_request.values.get('Body', None)

    person = get_person_by_phone_number(from_number, people)
    title = person.title
    first_name = person.first_name

    message = f"Message from {title} {first_name}: \n\n{body}"

    send(twilio_client, to_number, twilio_number, message)




@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    forward_message(client, admin_number, twilio_number, request)

    from_number = request.values.get('From', None)

    person = get_person_by_phone_number(from_number, people)

    response_message = get_personalized_response(person)

    response = MessagingResponse()
    response.message(response_message)

    return str(response)




if __name__ == '__main__':
    app.run(debug=True)