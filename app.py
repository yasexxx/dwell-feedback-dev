
import os
from flask import Flask, render_template
from flask_mongoengine import MongoEngine


app = Flask(__name__, template_folder='dowell_app/templates')

def select_env():
    env = os.getenv('ENV_OPT')
    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    else :
        app.config.from_object('config.DevelopmentConfig')

select_env()
mongodb = MongoEngine()
mongodb.init_app(app)

def create_app():
    from dowell_app.blueprints.home.views import home
    from dowell_app.blueprints.user.views import user
    # app.register_blueprint(blueprint=home)
    app.register_blueprint(blueprint=user, url_prefix="/user")
    return app

@app.route('/')
def index():
    return render_template('home.html')

from app import app


if __name__ == "__main__":
    create_app().run()