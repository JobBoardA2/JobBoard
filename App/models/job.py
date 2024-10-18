from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db

class Job(db.Model):
    # __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.recruiter_id'))
    # recruiters = db.relationship('Recruiter', back_populates='jobs')
    # recuiters = db.relationship(Recruiter, backref='job')
    # companies = db.relationship('Company', back_populates='listings', overlaps='company')


    applications = db.relationship('Application', backref='job')

    def __init__(self,recruiter_id, job_title, description, salary, location):
        self.recruiter_id = recruiter_id
        self.job_title = job_title
        self.description = description
        self.salary = salary
        self.location = location
        

    def view_job_details(self):
        return {
            # 'job_id': self.job_id,
            'job_title': self.job_title,
            'description': self.description,
            'salary': self.salary,
            'location': self.location
        }

# from App.models.recruiter import Recruiter