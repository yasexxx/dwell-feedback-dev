from os import name
from flask import Blueprint, render_template
from dowell_app.models.feedback import Feedback

home = Blueprint(name='home', import_name =__name__, template_folder='templates')

@home.route('/', methods=['GET'])
def home_page():
    fb_list = Feedback.objects()
    return render_template('home.html', fb_list=fb_list, enumerate=enumerate)