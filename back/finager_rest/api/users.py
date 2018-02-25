from sqlalchemy import exc
from flask import Blueprint, jsonify, request
from finager_rest.api.models import User
from finager_rest import db
from flask_swagger import swagger

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users/ping', methods=['GET'])

def ping_pong():
    """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: Ping
              properties:
                name:
                 type: string
                 description: Ping
        responses:
          200:
            description: User created
        """
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@users_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    response_object = {
        'status': 'fail',
        'message': 'Invalid payload.'
    }
    if not post_data:
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    password = post_data.get('password')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email, password=password))
            db.session.commit()
            response_object['status'] = 'success'
            response_object['message'] = f'{email} was added!'
            return jsonify(response_object), 201
        else:
            response_object['message'] = 'Sorry. That email already exists.'
            return jsonify(response_object), 400
    except (exc.IntegrityError, ValueError) as e:
        db.session.rollback()
        return jsonify(response_object), 400
