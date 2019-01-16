import logging


def create_logger(
    level = logging.INFO,
    format_string = '\n%(asctime)s: %(levelname)s:\n%(message)s',
    date_format_string = '%Y-%m-%d %H:%M:%S',
    file_path = 'test.txt'
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