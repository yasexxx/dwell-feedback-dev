from flask import Blueprint, json
from flask import request, jsonify
from dowell_app.models.feedback import Feedback

feedback = Blueprint('feedback', __name__)

@feedback.route('/', methods=['GET'])
def query_records():
    args = request.args
    print('ARGUMENTS: ', args)
    fb = Feedback.objects()
    if not fb:
        return jsonify({'error': 'Data not found', 'success': False}), 404
    else:
        return jsonify(fb.to_json(fb)), 200

@feedback.route('/', methods=['PUT'])
def create_feedback():
    record = json.loads(request.data)
    fb = Feedback(name=record['name'], project_id=record['project_id'], email=record['email'],  occupation=record['occupation'],
        feedback_1=record['feedback_1'], feedback_2=record['feedback_2'], total=record['total'],)
    fb.save()
    return jsonify({'message'})

@feedback.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = Feedback.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'Feedback on {} was not found'.format(record['name']), 'success': False})
    else:
        user.delete()
    return jsonify(user.to_json())