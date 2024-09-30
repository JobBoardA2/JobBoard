from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db
from App.models import Recruiter,Job,Applicatio,Applicant
from App import app
db = SQLAlchemy(app)

class Job(db.Model):
    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiters.recruiter_id'), nullable=False)

    applications = db.relationship('Application', backref='job', lazy=True)

    def view_job_details(self):
        return {
            'title': self.title,
            'description': self.description,
            'salary': self.salary,
            'location': self.location
        }