import os
from flask import Blueprint, json
from flask import request, jsonify
from dowell_app.models.feedback import Feedback

feedback = Blueprint('feedback', __name__)

@feedback.route('/', methods=['GET'])
def query_records():
    args = request.args
    print('ARGUMENTS: ', args)
    fb = Feedback.objects().exclude('id').exclude('created_at')
    if not fb:
        data = list()
        return jsonify(data), 200
    else:
        return jsonify(fb), 200

@feedback.route('/', methods=['PUT'])
def create_feedback():
    eid = request.args.get('eid')
    record = json.loads(request.data)
    s_key = os.getenv('ENCRYPT_KEY')
    if record and s_key == eid:
        fb = Feedback(name=record['name'], project_id=record['project_id'], email=record['email'],  occupation=record['occupation'],
            feedback_1=record['feedback_1'], feedback_2=record['feedback_2'], total=record['total'],)
        fb.save()
        return jsonify({'message': 'Feedback added with name {}'.format(record['name'])}), 200
    else:
        return jsonify({'message': 'Error unauthorized saving data endpoint'}), 401

@feedback.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = Feedback.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'Feedback on {} was not found'.format(record['name']), 'success': False})
    else:
        user.delete()
    return jsonify(user.to_json())