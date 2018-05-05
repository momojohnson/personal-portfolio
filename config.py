import os
class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development Configurations
    """
    
    SQLALCHEMY_ECHO = True
    
class ProductionConfig(Config):
    """
    Production Configurations
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
  
    DEBUG = False
    SQLALCHEMY_ECHO = False

app_config = {
'development': DevelopmentConfig,
'production': ProductionConfig
}
