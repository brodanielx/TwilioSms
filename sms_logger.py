import datetime
from foi import FOI
import logging
import os
from person import get_person_by_phone_number

people = FOI



def create_file_path(file_name_prefix):
    '''
    Create file path for log file with today's date in the name.
    Ex: sms_012419.log
    '''
    today_string = datetime.datetime.today().strftime('_%Y_%m_%d')
    file_name = f'{file_name_prefix}{today_string}.log'
    return os.path.join('logs', file_name)


def create_logger(
    level = logging.INFO,
    format_string = '\n%(asctime)s: %(levelname)s:\n%(message)s',
    date_format_string = '%Y-%m-%d %H:%M:%S',
    file_path = 'test.log'
    ):
    '''
    Create logger object
    '''

    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    formatter = logging.Formatter(format_string, date_format_string)
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

    

def format_incoming_sms_request(request):
    date_created_string = datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")

    from_number = request.values.get('From', None)
    from_person = get_person_by_phone_number(from_number, people)

    to_number = request.values.get('To', None)
    to_person = get_person_by_phone_number(to_number, people)

    body = request.values.get('Body', None)

    formatted_log_entry = format_log_entry(body, date_created_string, from_person, to_person)

    return formatted_log_entry




def format_twilio_message_instance(twilio_message_instance):
    '''
    Create human readable representation of a Twilio Message Response
    '''

    properties = twilio_message_instance.__dict__['_properties']

    date_created = properties['date_created']
    date_created_string = f'{date_created.strftime("%m/%d/%y %H:%M:%S")} (UTC)'

    from_number = properties['from_']
    from_person = get_person_by_phone_number(from_number, people)

    to_number = properties['to']
    to_person = get_person_by_phone_number(to_number, people)

    body = properties['body']

    formatted_log_entry = format_log_entry(body, date_created_string, from_person, to_person)

    return formatted_log_entry



def format_log_entry(body, date_created_string, from_person, to_person):
    return f'Date sent: {date_created_string} \nFrom: {from_person.full_name} ({from_person.phone_number}) \nTo: {to_person.full_name} ({to_person.phone_number}) \n\nMessage: \n{body}\n'
