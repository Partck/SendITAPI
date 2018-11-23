import os

class Config(object):
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

class TestingConfig(Config):
    DEBUG = True
    url = "dbname = 'test_senditdb' host = 'localhost' port = '5432'\
     user = 'sendit_user' password = 'qwerty'"


class DevelopmentConfig(Config):
    DEBUG = True
    url = os.getenv("URL")
    



config={"test":TestingConfig,
        "dev":DevelopmentConfig}
