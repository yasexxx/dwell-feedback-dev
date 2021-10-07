
import os
from flask import Flask
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

from app import app

def create_app():
    from dowell_app.blueprints.home.views import home
    from dowell_app.blueprints.user.views import user
    from dowell_app.blueprints.feedback.views import feedback
    app.register_blueprint(home)
    app.register_blueprint(user, name='user', url_prefix='/user')
    app.register_blueprint(feedback, url_prefix='/feedback')
    return app
    
if __name__ == "__main__":
    create_app().run()