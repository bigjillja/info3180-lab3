import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = "jinchuriki"
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_PORT = 465
    MAIL_USERNAME = "0ae243f3a66ccd"
    MAIL_PASSWORD = "ea1cd742e0085f"
