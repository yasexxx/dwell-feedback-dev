from flask import Blueprint, render_template, session, request
from flask import json
from flask.helpers import url_for
from flask.json import jsonify
from dowell_app.models.feedback import Feedback

home = Blueprint(name='home', import_name =__name__, template_folder='templates')

@home.route('/', methods=['GET'])
def home_page():
    fb_list = Feedback.objects()
    return render_template('home.html', fb_list=fb_list, enumerate=enumerate)

@home.route('/public-api/feedback-extension', methods=['GET'])
def get_len_feedback():
    fb_list = Feedback.objects()
    len_fb = len(fb_list)
    return jsonify(len_fb), 200
