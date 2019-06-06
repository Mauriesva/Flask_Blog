from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


# import secrets para formulario
# secrets.token_hex(16)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

'''Antes
# import secrets para formulario
# secrets.token_hex(16)
# En terminal añadir las variables : touch ~/.bash_profile, open ~/.bash_profile, source ~/.bash_profile

app.config['SECRET_KEY'] = '112312323423423asda2'
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

app.config['MAIL_USERNAME'] = "correo@gmail.com"
app.config['MAIL_PASSWORD'] = 'contrasenya'
'''

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


# crear la bd a partir de los modelos
# python3
# from flaskblog import db
# db.create_all()
# probando desde el terminal
# from flaskblog import User, Post
# user_1 = User(username='Mauricio', email='mauricio@gmail.com', password = 'password')
# db.session.add(user_1)
# <User (transient 4460265368)>
# una vez creado todos :
# db.session.commit()
# User.query.all() vemos todos User.query.first() , User.query.filter_by(username='Mauricio').all(), user = User.query.get(1)
# user.id    1
# post_1 = Post(title='Blog 1',content= 'First Post Content!',user_id=user.id)
# db.session.add(post_1)
# db.session.commit()
# user.posts
# [<Post 1>]
# for post in user.posts:
#     print(post.date_posted)
# 2019-04-19 09:49:42.280683
# post = Post.query.first()
# post.user_id
# post.author

# db.drop_all()
# db.create_all()

# User.query.all()
# Post.query.all()

# CREAMOS LA BASE DE DATOS A PARTIR DE LOS MODELOS
# from flaskblog import db
# from flaskblog.models import User, Post
# db.create_all()
