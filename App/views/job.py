from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from App.controllers.job import create_job, get_all_jobs_json
from App.models import db

job_views = Blueprint('job_views', __name__, template_folder='../templates')


# Endpoint to create a job
@job_views.route('/api/jobs', methods=['POST'])
@jwt_required()
def create_job_endpoint():
    data = request.json
    recruiter_id = data.get('recruiter_id')
    job_title = data.get('job_title')
    description = data.get('description')
    salary = data.get('salary')
    location = data.get('location')

    if not (recruiter_id and job_title and description and salary and location):
        return jsonify({'message': 'Missing required fields'}), 400

    create_job(recruiter_id, job_title, description, salary, location)
    return jsonify({'message': f"Job '{job_title}' created successfully"}), 201


# Endpoint to get all jobs
@job_views.route('/api/jobs', methods=['GET'])
@jwt_required()
def get_jobs_endpoint():
    jobs = get_all_jobs_json()
    return jsonify(jobs), 200
