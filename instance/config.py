import os

class Config(object):
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

class TestingConfig(Config):
    DEBUG = True
    url =" dbname = 'd8osr4jq6ahd25' host = 'ec2-54-204-36-249.compute-1.amazonaws.com' port = '5432'\
        user = 'jkaegobpsrhntk' password = 'ee912001d1be919a6e88385a69e75f54f4c757ca9ca5293ea25e28b29d267148'"


class DevelopmentConfig(Config):
    DEBUG = True
    url = os.getenv("URL")
    



config={"test":TestingConfig,
        "dev":DevelopmentConfig}


    