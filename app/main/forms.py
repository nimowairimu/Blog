class UserProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    profile_pic_path = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

class BlogForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Post')