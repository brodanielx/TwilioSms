# TwilioSms

## Send SMS
1. Update list of phone numbers to send to
    - FOI in foi.py
2. Update message in message.py
    - Use a gmail draft to compose message. Using iCloud Notes will causes errors in the order in which the messages are delivered.
    - For first few messages sent, test by ony sending to my number first.
3. Run send_sms.py

## Receive SMS
1. Update list of phone numbers
    - FOI in foi.py
2. Run ./ngrok http 5000 in dev folder
3. Phone Numbers => Messaging => A Message Comes In
    - copy ngrok link into "A Message Comes In" field and add "/sms" to ngrok link
4. Run receive_sms.py

### ToDo
- Fix logger - receive_sms creating duplicate entries in log
- automate running of scripts
    - shebang line
- Configure for running on OS and Windows
- Work on sending images
