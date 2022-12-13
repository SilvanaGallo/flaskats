import os
from dotenv import load_dotenv
    
class Config:
    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BROKER_HOST = os.environ.get('BROKER_HOST')

    #MAILER
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    #MAIL_DEBUG = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_API_KEY')
    MAIL_DEFAULT_SENDER = "usefulapp2022@outlook.com"
    MAIL_MAX_EMAILS = None
    #MAIL_SUPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False

    #REPOSITORY
    REPOSITORY_TOKEN = os.environ.get('REPOSITORY_TOKEN')
    BASE_ID = os.environ.get('BASE_ID')
    TABLE_NAME = os.environ.get('TABLE_NAME')