from flask import Blueprint, current_app, jsonify

http = Blueprint(name="businessml", import_name=__name__, url_prefix="/api")

@http.route('/status')
def application_status():
    return jsonify({'status':'Server is up and running'})

