from flask import Blueprint


@swagger_blueprint.route('/swagger/api', methods=['POST'])
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)
