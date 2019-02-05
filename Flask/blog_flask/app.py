from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

from flask import redirect, url_for, request


# define main flask app
app = Flask(__name__)
app.config.from_object(Configuration)

# define ORM and pass there our app
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### Admin ###
from models import *


# create mixin who connected AdminView and HomeAdminView
class AdminMixin:
	def is_accessible(self):
		return current_user.has_role('admin')

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
    # create option auto slug generate with admin panel
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


# class who inherit AdminMixin and ModelView properties
class AdminView(AdminMixin, ModelView):
	pass


# class who inherit AdminMixin and AdminIndexView properties
class HomeAdminView(AdminMixin, AdminIndexView):
	pass


# for admin panel in post create menu view fields
class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title', 'body', 'tags']


# for admin panel in tag create menu view fields
class TagAdminView(AdminMixin, BaseModelView):
    form_columns = ['name', 'posts']


admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
# contact Post with admin panel
admin.add_view(PostAdminView(Post, db.session))
# contact Tag with admin panel
admin.add_view(TagAdminView(Tag, db.session))


### Flask Security ###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)