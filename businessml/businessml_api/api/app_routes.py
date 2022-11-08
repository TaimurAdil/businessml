from flask import Blueprint, current_app, jsonify
from random import randint, random
import mlflow
from mlflow import log_metric, log_param, log_artifacts

http = Blueprint(name="businessml", import_name=__name__, url_prefix="/api")


@http.route('/status')
def application_status():
    return jsonify({'status':'Server is up and running'})

@http.route('/sample_run')
def sample_run():
    
    mlflow.set_tracking_uri('http://mlflow:5000')
    log_param("param1", randint(0, 100))
    log_metric("foo", random())
    log_metric("foo", random() +1)
    log_metric("foo", random() +2)

    return jsonify({'status':'sample run execution completed,  ${MLFLOW_TRACKING_URI}'})
