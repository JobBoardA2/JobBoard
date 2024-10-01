from App.models.job import Job
from App.models.recruiter import Recruiter
from App.database import db

def create_job(recruiter_id, job_title,description, salary, location):
    recruiter = Recruiter.query.get(recruiter_id)
    if recruiter:
        job = Job(
            recruiter_id=recruiter_id,
            job_title=job_title,
            description= description,
            salary=salary,
            location=location,
        )
        db.session.add(job)
        db.session.commit()
        print(f"Job '{job_title}' created for recruiter {recruiter.name}")
    else:
         print(f"Recruiter with ID {recruiter_id} not found.")

def get_all_jobs():
    return Job.query.all()

def get_all_jobs_json():
    jobs = Job.query.all()
    if not jobs:
        return []
    jobs = [job.view_job_details() for job in jobs]
    return jobs 