import os
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://felista:ilovemyself@localhost/blog'  
#    email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nimo:kadesho62@localhost/blog'
    DEBUG = True



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}  