from flask import jsonify, make_response
# from app.models import User
from app.api import bp


@bp.route('/employees', methods=['GET'])
def get_employees():
  return make_response(jsonify({'message': 'test employee route'}), 200)
