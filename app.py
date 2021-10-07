
import os
from flask import Flask, url_for
from flask_mongoengine import MongoEngine

app = Flask(__name__, static_url_path='/', static_folder='dowell_app/static')

def select_env():
    env = os.getenv('ENV_OPT')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else :
        app.config.from_object('config.DevelopmentConfig')

select_env()
mongodb = MongoEngine()
mongodb.init_app(app)

from app import app

# app.add_url_rule('/favicon.ico',
#                  redirect_to=url_for('static', filename='favicon.ico'))
    
from dowell_app.blueprints.home.home import home
from dowell_app.blueprints.user.user import user
from dowell_app.blueprints.feedback.feedback import feedback

api_prefix = os.getenv('PREFIX_API')

app.register_blueprint(home)
app.register_blueprint(user, url_prefix=f'{api_prefix}/user')
app.register_blueprint(feedback, url_prefix=f'{api_prefix}/feedback')

if __name__ == "__main__":
    app.run()