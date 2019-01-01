import os
from flask import Flask, request, redirect
from phone_numbers import FORWARD_NUMBER
from pprint import pprint
from response import RESPONSE_BODY
from send_sms import send
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio_variables import *


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

forward_number = FORWARD_NUMBER
twilio_number = TWILIO_PHONE_NUMBER

app = Flask(__name__)

def forward_message(twilio_client, to_number, twilio_number, twilio_request):

    from_number = twilio_request.values.get('From', None)

    body = twilio_request.values.get('Body', None)

    message = f"Message from {from_number}: \n\n{body}"

    send(twilio_client, to_number, twilio_number, message)




@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():

    pprint(request.values.__dict__, indent=2)

    forward_message(client, forward_number, twilio_number, request)

    response = MessagingResponse()
    response.message(RESPONSE_BODY)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)