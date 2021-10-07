from flask import Blueprint, json
from flask import request, jsonify
from dowell_app.models.user import User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'Data not found', 'success': False})
    else:
        return jsonify(user.to_json())

@user.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@user.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'Data not found', 'success': False})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@user.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'Data not found', 'success': False})
    else:
        user.delete()
    return jsonify(user.to_json())