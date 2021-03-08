from . import db
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True)
    bio = db.Column(db.String(255)
    profile_pic_path = db.Column(db.String(150) 
    pass_secure = db.Column(db.String(255)
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')


    #  @property
    # def set_password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @set_password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)


    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)
    
    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
 
  
    # def __repr__(self):
    #     return f'User {self.username}'

class Quote:
    '''
    Quote class to define Movie Objects
    '''

    def __init__(self,id,quote,author):
        self.id =id
        self.quote = quote
        self.author = author
       