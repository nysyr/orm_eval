import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_URL = os.environ.get('POSTGRES_URL')
POSTGRES_DB = os.environ.get('POSTGRES_DB')

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{usr}:{passwd}@{host}/{db}'.format(
        usr=POSTGRES_USER, passwd=POSTGRES_PASSWORD, host=POSTGRES_URL, db=POSTGRES_DB)
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oreilly:hunter2@postgres:5432/oreilly'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False