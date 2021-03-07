from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Quote:
    '''
    Quote class to define Movie Objects
    '''

    def __init__(self,id,quote,author):
        self.id =id
        self.quote = quote
        self.author = author
       