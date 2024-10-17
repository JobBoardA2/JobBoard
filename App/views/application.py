from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from App.controllers.application import create_application, get_all_applications_json

application_views = Blueprint('application_views', __name__, template_folder='../templates')


# Endpoint to apply for a job
@application_views.route('/api/applications', methods=['POST'])
@jwt_required()
def create_application_endpoint():
    data = request.json
    job_id = data.get('job_id')
    applicant_id = data.get('applicant_id')

    if not (job_id and applicant_id):
        return jsonify({'message': 'Missing required fields'}), 400

    response, status = create_application(job_id, applicant_id)
    return jsonify(response), status


# Endpoint to view all applications
@application_views.route('/api/applications', methods=['GET'])
@jwt_required()
def get_applications_endpoint():
    applications = get_all_applications_json()
    return jsonify(applications), 200
