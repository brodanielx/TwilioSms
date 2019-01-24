import datetime
import logging
import os



def create_file_path():
    '''
    Create file path for log file with today's date in the name.
    Ex: sms_012419.log
    '''
    today_string = datetime.datetime.today().strftime('_%m%d%y')
    file_name = f'sms{today_string}.log'
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
