from dotenv import load_dotenv
import logging
from os import environ

def initialize() :
    logging.info('Running locally, loading .env file')
    load_dotenv(verbose=True)
    print(environ.get('bootstrap.servers'))
    print(environ.get('sasl.mechanisms'))
    print(environ.get('security.protocol'))
    print(environ.get('sasl.username'))
    print(environ.get('sasl.password'))
    print(environ.get('topic'))