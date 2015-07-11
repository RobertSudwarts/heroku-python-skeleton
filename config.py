
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    # DATABASE_URI = 'sqlite://:memory:'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://temp.db'

class TestingConfig(Config):
    TESTING = True

    

