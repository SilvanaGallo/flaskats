import os
from dotenv import load_dotenv
    
class Config:
    load_dotenv()
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BROKER_HOST = os.environ.get('BROKER_HOST')

    #MAILER
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    #REPOSITORY
    REPOSITORY_TOKEN = os.environ.get('REPOSITORY_TOKEN')
    BASE_ID = os.environ.get('BASE_ID')
    TABLE_NAME = os.environ.get('TABLE_NAME')