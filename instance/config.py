import os

class Config(object):
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

class TestingConfig(Config):
    DEBUG = True
    url ="dbname = 'dfhkvc5kqeh9bi' host = 'ec2-54-235-156-60.compute-1.amazonaws.com' port = '5432' \
        user = 'ehiewszseuqzyg' password = 'aff8667735390b9eebe291e92f4ad1d75a255aeefc38b8382f368e7a2a0650bd'"

class DevelopmentConfig(Config):
    DEBUG = True
    url = os.getenv("URL")
    



config={"test":TestingConfig,
        "dev":DevelopmentConfig}


    