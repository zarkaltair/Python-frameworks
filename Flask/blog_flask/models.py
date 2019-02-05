from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin


# difine function which forms slug
def slugify(s):
    # string with r it is raw string
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


# this variable is class instance Table
# post_tags is name of table in database
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


# create class which forms post and save their to database
class Post(db.Model):
    # define propertis of post
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    # *args it is list of arguments
    # **kwargs it is dict of named argument (key words) 
    def __init__(self, *args, **kwargs):
        # call super class from Post and get class instance
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    # create relationship between tags and posts
    # 'Tag' is name of table in db
    # lazy='dynamic' extands functionl standart list, type=BaseQuery
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))


    # function which generate slug
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    # function that converts our output for convenience
    def __repr__(self):
        return '<Post id {}, title: {}>'.format(self.id, self.title)


# create class which forms tag
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    # function which generate slug
    def __init__(self, *args, **kwargs):
        # call super class from Tag and get class instance
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    # function that converts our output for convenience
    def __repr__(self):
        return '{}'.format(self.name)


### Flask security ###

# create new table which define users and thier roles
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )


# create class user with his properties
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


# define users roles
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))