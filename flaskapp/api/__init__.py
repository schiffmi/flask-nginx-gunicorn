from flask import Blueprint, jsonify

api = Blueprint('api', __name__, 
					static_folder=None, 
					static_url_path=None,
					template_folder=None)

@api.route('/')
def apihome():
  return jsonify({'boom':'shakalaka'})