import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or 'my_secret_pass_code_hard_to_crack'

class TestingConfig(Config):
    DEBUG = True
