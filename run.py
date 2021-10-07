
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
mongodb = MongoEngine()
mongodb.init_app(app)

def create_app():

    from dowell_app.blueprints.user.views import user
    from dowell_app.blueprints.home.views import home
    app.register_blueprint(blueprint=user, url_prefix="/user")
    app.register_blueprint(blueprint=home)
    
    return app

if __name__ == "__main__":
    create_app().run()