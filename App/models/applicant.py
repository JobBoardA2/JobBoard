from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func 
from App.database import db
from App.models.job import Job
from App.models.application import Application


class Applicant(db.Model):
    # __tablename__ = 'applicant'

    applicant_id = db.Column(db.Integer, primary_key=True ,autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    applications = db.relationship('Application', backref='applicant', lazy=True)
    def __init__(self,name,email):
            self.name = name
            self.email = email
    
    def view_applicant_details(self):
        return{
            'applicant_id':self.applicant_id,
            'name':self.name,
            'email':self.email
        }