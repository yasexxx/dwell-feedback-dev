from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/home')

@home.route('/', methods=['GET'])
def home_page():
    return 'Home Webpage'