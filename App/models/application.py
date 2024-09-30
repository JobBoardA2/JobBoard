from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db
from App import app
from App.models import Recruiter,Job,Application,Applicant
db = SQLAlchemy(app)

class Application(db.Model):
    __tablename__ = 'applications'

    application_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.jobID'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('job_seekers.seekerID'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')

    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()

    def to_dict(self):
        return {
            'application_id': self.application_id,
            'job_id': self.job_id,
            'applicant_id': self.applicant_id,
            'applicationDate': self.applicationDate,
            'status': self.status
        }