from flask import Blueprint, render_template

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/', methods=['GET'])
def home_page():
    return render_template('home.html')