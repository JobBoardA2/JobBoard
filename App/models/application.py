from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db

class Application(db.Model):
    # __tablename__ = 'applications'

    application_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.job_id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.applicant_id'), nullable=False)
    
    def __init__(self,job_id,applicant_id):
        self.job_id = job_id
        self.applicant_id = applicant_id

    def view_application_details(self):
        return {
            'application_id': self.application_id,
            'job_id': self.job_id,
            'applicant_id': self.applicant_id,
        }