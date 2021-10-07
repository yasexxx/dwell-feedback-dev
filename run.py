
import os
from flask import Flask
from flask_mongoengine import MongoEngine

def select_env():
    env = os.getenv('ENV_OPT')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else :
        app.config.from_object('config.DevelopmentConfig')

def create_app():

    from dowell_app.blueprints.user.views import user
    from dowell_app.blueprints.home.views import home
    app.register_blueprint(blueprint=user, url_prefix="/user")
    app.register_blueprint(blueprint=home)
    
    return app

app = Flask(__name__)
select_env()
mongodb = MongoEngine()
mongodb.init_app(app)


if __name__ == "__main__":
    create_app().run()