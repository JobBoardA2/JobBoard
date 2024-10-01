from App.models.applicant import Applicant
from App.models.application import Application
from App.models.job import Job
from App.models.recruiter import Recruiter
from App.database import db

def create_applicant(name, email):
    applicant = Applicant(name=name, email=email)
    db.session.add(applicant)
    db.session.commit()
    return applicant

def get_all_applicants():
    return Applicant.query.all()

def get_all_applicants_json():
    applicants = Applicant.query.all()
    if not applicants:
        return []
    applicants = [applicant.view_appliant_details() for applicant in applicants]
    return applicants

def get_all_jobs_json():
    jobs = Job.query.all()
    if not jobs:
        return []
    jobs = [job.view_job_details() for job in jobs]
    return jobs 

def get_all_recruiters_json():
    recruiters = Recruiter.query.all()
    if not recruiters:
        return []
    recruiters = [recruiter.view_recruiters_details() for recruiter in recruiters]
    return recruiters

def get_all_applications_json():
    applications = Application.query.all()
    if not applications:
        return []
    applications = [application.view_appliant_details() for application in applications]
    return applications 