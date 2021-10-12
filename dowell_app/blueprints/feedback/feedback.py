from datetime import datetime
from json.decoder import JSONDecodeError
import os
from flask import Blueprint, json
from flask import request, jsonify
from dowell_app.models.feedback import Feedback
import json as json_

feedback = Blueprint('feedback', __name__)

@feedback.route('/', methods=['GET'])
def query_records():
    args = request.args
    fb = Feedback.objects().exclude('id').exclude('created_at')
    if not fb:
        data = list()
        return jsonify(data), 200
    else:
        return jsonify(fb), 200

@feedback.route('/', methods=['PUT'])
def create_feedback():
    eid = request.args.get('eid')
    print("REQUEST: ", request.data)
    print(type(request.data))
    try:
        record = json.loads(request.data)
    except JSONDecodeError:
        req_data = (request.data).decode('utf-8')
        print("DATA: ",req_data)
        record = json.loads(req_data) 
    print(record)
    s_key = os.getenv('ENCRYPT_KEY')
    if record and s_key == eid:
        fb = Feedback(si_number=record['si_number'], date=record['date'], project_number=record['project_number'],  
            name=record['name'], phone=record['phone'], email=record['email'], dowellID=record['dowellID'], 
            country=record['country'], role=record['role'], q01=record['q01'], q02=record['q02'], q03=record['q03'],
            q04=record['q04'], q05=record['q05'], q06=record['q06'], q07=record['q07'], q08=record['q08'],
            q09=record['q09'], q10=record['q10'], q11=record['q11'], q12=record['q12'], q13=record['q13'],
            q14=record['q14'], total=record['total'], percentage=record['percentage'], feedback1=record['feedback1'], 
            feedback2=record['feedback2'])
        fb.save()
        return jsonify({'message': 'Feedback added with SI Number {}'.format(record['si_number'])}), 200
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