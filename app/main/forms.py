from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError
from wtforms.validators import Required,Email
from flask_login import current_user
from ..models import User

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Blog review', validators=[Required()])
    submit = StringField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating a blog
    '''
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')
class CommentForm(FlaskForm):
    '''
    Class to create a wtf form for creating a blog
    '''
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')
class BlogForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    content = TextAreaField('YOUR BLOG')
    submit = SubmitField('CREATE')
