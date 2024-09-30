from App.models import Recruiter,Job,Application,Applicant
from App.database import db

def create_recruiter(recruiter_id,name,email,company_name):
    
    if not recruiter_id or not name or not email or not company_name:
        return jsonify({'message': 'All fields are required'}), 400

    recruiter = Recruiter(recruiter_id=recruiter_id, name=name, email=email, company_name=company_name)
    
    db.session.add(recruiter)
    db.session.commit()
    
    return jsonify({'message': f'Recruiter {name} created with ID: {recruiter.recruiter_id}'}), 201

def create_job(recruiter_id):
    data = request.json
    recruiter = Recruiter.query.get(recruiter_id)
    if not recruiter:
        return jsonify({'message': 'Recruiter not found'}), 404
    
    job = recruiter.create_job(
        title=data['title'],
        description=data['description'],
        salary=data['salary'],
        location=data['location']
    )
    return jsonify({'message': 'Job created', 'job': job.job_id}), 201