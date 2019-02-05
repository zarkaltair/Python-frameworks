from wtforms import Form, StringField, TextAreaField


# create form for rerquest on make post
class PostForm(Form):
    # class instance which define field title
    title = StringField('Title')
    # class instance which define field body
    body = TextAreaField('Body')