from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from App.controllers.applicant import create_applicant, get_all_applicants_json

applicant_views = Blueprint('applicant_views', __name__, template_folder='../templates')


# Endpoint to create an applicant
@applicant_views.route('/api/applicants', methods=['POST'])
@jwt_required()
def create_applicant_endpoint():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not (name and email):
        return jsonify({'message': 'Missing required fields'}), 400

    applicant = create_applicant(name, email)
    return jsonify({'message': f"Applicant '{applicant.name}' created successfully"}), 201


# Endpoint to get all applicants
@applicant_views.route('/api/applicants', methods=['GET'])
@jwt_required()
def get_applicants_endpoint():
    applicants = get_all_applicants_json()
    return jsonify(applicants), 200
