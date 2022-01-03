from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# To prevent from various attacks
app.config['SECRET_KEY'] = '967d1767432f72c86aab457ed23dcf7d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # To tell our extension "login_required" where are login route is located
login_manager.login_message_category = 'info'

from flaskblog import routes