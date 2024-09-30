from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db
from App.models import Recruiter,Job,Application,Applicant

class Recruiter(db.Model):
    recruiter_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    email = db.column(db.String(120),unique=True,nullable=False)
    company_name = db.column(db.String(120), nullable=False)
    jobs = db.relationship('Job', backref='recruiter', lazy=True)  # Relationship with Job
    
    def __init__(self,recruiter_id,name,email,company_name):
        self.recruiter_id = recruiter_id
        self.name = name
        self.email = email
        self.company_name = company_name

        def create_job(self, job_title, job_description, salary, location):
            new_job = Job(
                title=job_title,
                description=job_description,
                salary=salary,
                location=location,
                recruiter_id=self.id,  
            )
            db.session.add(new_job)
            db.session.commit()
            return new_job

    def view_job_applicants(self, job_id):
        job = Job.query.filter_by(jobID=job_id, recruiter_id=self.recruiter_id).first()
        if job:
            applications = Application.query.filter_by(jobID=job_id).all()
            return [application.to_dict() for application in applications]
        return []
