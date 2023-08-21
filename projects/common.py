import random
import string
import logging


def generate_txn_id(length=None):
    if not length:
        length = 35
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    logging.info("The randomly generated string is : " + str(random_string))
    return random_string
