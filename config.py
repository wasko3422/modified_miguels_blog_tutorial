import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY") or 'try and find out what the secret key is'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get("MAIL_PORT"))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'

