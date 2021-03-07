class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nimo:kadesho62@localhost/bloggitvadd'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
