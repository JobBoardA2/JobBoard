import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.controllers.applicant import create_applicant, get_all_applicants_json, get_all_applications_json
from App.controllers.application import create_application
from App.controllers.job import create_job, get_all_jobs, get_all_jobs_json
from App.controllers.recruiter import create_recruiter, get_all_recruiters, get_all_recruiters_json
from App.main import create_app
from App.database import db, create_db
from App.models import User
from App.models import Recruiter
from App.controllers import *
from App.models import Job
from App.models import Applicant
from App.models import Application
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass")
        assert user.username == "bob"

    # pure function no side effects or integrations called
    def test_get_json(self):
        user = User("bob", "bobpass")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

class RecruiterUnitTests(unittest.TestCase):
    def test_new_Recruiter(self):
        recruiter = Recruiter("Jane Doe","JaneDoe@mail.com","Cloud.Inc")
        assert recruiter.name == "Jane Doe"

    def test_Recruiter_get_json(self):
        recruiter = Recruiter("Jane Doe","JaneDoe@mail.com","Cloud.Inc")
        recruiter_json = recruiter.view_recruiters_details()
        expected_recruiter_json = {
        'recruiter_id': None,
        "name": "Jane Doe",
        "email": "JaneDoe@mail.com",
        "company_name": "Cloud.Inc"
        }
        self.assertDictEqual(recruiter_json,expected_recruiter_json)

    def test_get_all_recruiters(self):
        recruiter = Recruiter("Jane Doe","jane@example.com","Cloud Inc.")
        expected_output = {'recruiter_id': None,"name": "Jane Doe", "email": "jane@example.com", "company_name": "Cloud Inc."}
        actual_output = recruiter.view_recruiters_details()
        self.assertEqual(actual_output, expected_output)

class JobUnitTests(unittest.TestCase):

    def test_create_Job(self):
        job = Job(1,"Software Engineer", "Develop applications" ,120000 ,"New York") 
        assert job.job_title == "Software Engineer"

    def test_get_all_jobs_json(self):
        job = Job(1,"Software Engineer", "Develop applications" ,120000 ,"New York") 
        expected_output = {"job_title":"Software Engineer" ,"description":"Develop applications", "salary":120000, "location":"New York"}
        actual_output = job.view_job_details()
        self.assertDictEqual(actual_output,expected_output)

    def test_get_all_jobs(self):
        job = Job(1,"Software Engineer", "Develop applications" ,120000 ,"New York") 
        expected_output = {"job_title":"Software Engineer" ,"description":"Develop applications", "salary":120000, "location":"New York"}
        actual_output = job.view_job_details()
        self.assertEqual(actual_output,expected_output)

class ApplicantUnitTests(unittest.TestCase):

    def test_create_applicant(self):
        applicant = Applicant("Jane Doe","JaneDoe@gmail.com")
        assert applicant.name == "Jane Doe"

    def test_get_all_applicants_json(self):
        applicant = Applicant("Jane Doe","JaneDoe@gmail.com")
        expected_output = {"applicant_id":None,"name":"Jane Doe","email":"JaneDoe@gmail.com"}
        actual_output = applicant.view_applicant_details()
        self.assertDictEqual(actual_output,expected_output)

    def test_get_all_applicants(self):
        applicant = Applicant("Jane Doe","JaneDoe@gmail.com")
        expected_output = {"applicant_id":None ,"name":"Jane Doe","email":"JaneDoe@gmail.com"}
        actual_output = applicant.view_applicant_details()
        self.assertEqual(actual_output,expected_output)

class ApplicationUnitTests(unittest.TestCase):
    def test_create_application(self):

        application = Application(1,1)
        application.application_id = 1

        assert application.application_id == 1

    def test_get_all_applications_json(self):
        application = Application(1,1)
        expected_output = {            
            'application_id': 1,
            'job_id': 1,
            'applicant_id': 1
         }
        application.application_id = 1
        actual_output = application.view_application_details()
        self.assertEqual(actual_output,expected_output)

    def test_get_all_applications(self):
        application = Application(1,1)
        expected_output = {            
            'application_id': 1,
            'job_id': 1,
            'applicant_id': 1
         }
        application.application_id = 1
        actual_output = application.view_application_details()
        self.assertEqual(actual_output,expected_output)   









'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass")
    
    assert login("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"


class RecruiterIntegrationTests(unittest.TestCase):

    def test_create_recruiter(self):
        recruiter = create_recruiter("Jane Doe","JaneDoe@mail.com","Cloud.Inc")
        assert recruiter.name == "Jane Doe"

    def test_get_all_recruiters_json(self):
        recruiter_json = get_all_recruiters_json()
        expected = [{"recruiter_id": 1, "name": "Jane Doe", "email": "JaneDoe@mail.com", "company_name": "Cloud.Inc"}]
        self.assertListEqual(expected, recruiter_json)


class JobIntegrationTest(unittest.TestCase):
    
    def test_create_Job(self):
        job = create_job(1,"Software Engineer", "Develop applications" ,120000 ,"New York") 
        assert job.job_title == "Software Engineer"

    def test_get_all_jobs(self):
        jobs = get_all_jobs()  # This returns a list of Job objects
        job = jobs[0]  # Get the first job object from the list

        expected_output = {"job_id": 1, "job_title": "Software Engineer", "description": "Develop applications", "salary": 120000, "location": "New York"}
        
        # Compare the attributes of the job object with the expected output
        self.assertEqual(job.job_id, expected_output["job_id"])
        self.assertEqual(job.job_title, expected_output["job_title"])
        self.assertEqual(job.description, expected_output["description"])
        self.assertEqual(job.salary, expected_output["salary"])
        self.assertEqual(job.location, expected_output["location"])

class ApplicantIntegrationTest(unittest.TestCase):

    def test_create_applicant(self):
        applicant = create_applicant("Jane Doe","JaneDoe@gmail.com")
        assert applicant.name == "Jane Doe"

    def test_get_all_applicants_json(self):
        applicants = get_all_applicants_json()  # This returns a list of dictionaries
        applicant = applicants[0]  # Get the first applicant from the list

        expected_output = {"applicant_id": 1, "name": "Jane Doe", "email": "JaneDoe@gmail.com"}

         # Use assertDictEqual to compare dictionaries
        self.assertDictEqual(applicant, expected_output)


class ApplicationIntegrationTests(unittest.TestCase):

    def test_create_applicantion(self):
        application = create_application(1,1)
        assert application.applicant_id == 1

    def test_get_all_applications_json(self):
        expected_output = [{            
            'application_id': 1,
            'job_id': 1,
            'applicant_id': 1
         }]
        actual_output = get_all_applications_json()
        self.assertEqual(actual_output,expected_output)
    

    