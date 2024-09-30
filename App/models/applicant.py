from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db
from App.models import Recruiter,Job,Application,Applicant
from App import app
db = SQLAlchemy(app)

class Applicant(db.Model):
    __tablename__ = 'applicant'

    applicant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    applications = db.relationship('Application', backref='applicant', lazy=True)

    def apply_to_job(self, job_id):
        new_application = Application(
            job_id=job_id,
            applicant_id=self.seekerID,
            status='Pending'
        )
        db.session.add(new_application)
        db.session.commit()
        return new_application

    def view_jobs(self):
        return Job.query.all()