from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from App.controllers.recruiter import create_recruiter, get_all_recruiters_json

recruiter_views = Blueprint('recruiter_views', __name__, template_folder='../templates')


# Endpoint to create a recruiter
@recruiter_views.route('/api/recruiters', methods=['POST'])
@jwt_required()
def create_recruiter_endpoint():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    company_name = data.get('company_name')

    if not (name and email and company_name):
        return jsonify({'message': 'Missing required fields'}), 400

    recruiter = create_recruiter(name, email, company_name)
    return jsonify({'message': f"Recruiter '{recruiter.name}' created successfully", 'id': recruiter.recruiter_id}), 201


# Endpoint to get all recruiters
@recruiter_views.route('/api/recruiters', methods=['GET'])
@jwt_required()
def get_recruiters_endpoint():
    recruiters = get_all_recruiters_json()
    return jsonify(recruiters), 200
