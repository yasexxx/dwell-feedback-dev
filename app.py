
import os
from flask import Flask, render_template
from flask_mongoengine import MongoEngine


app = Flask(__name__)

def select_env():
    env = os.getenv('ENV_OPT')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else :
        app.config.from_object('config.DevelopmentConfig')

select_env()
mongodb = MongoEngine()
mongodb.init_app(app)

# @app.route('/')
# def index():
#     return render_template('home.html')


from dowell_app.blueprints.home.home import home
from dowell_app.blueprints.user.user import user
app.register_blueprint(home)
app.register_blueprint(user, url_prefix='/user')

def create_app():
    return app

from app import app


if __name__ == "__main__":
    create_app().run()