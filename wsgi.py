import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.controllers.recruiter import create_recruiter,get_all_recruiters,get_all_recruiters_json
from App.controllers.job import create_job,get_all_jobs,get_all_jobs_json
from App.controllers.application import create_application,get_all_applications,get_all_applications_json
from App.controllers.applicant import create_applicant,get_all_applicants,get_all_applicants_json
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

# Create an AppGroup for recruiter commands
recruiter_cli = AppGroup('recruiter', help='Recruiter object commands')

@recruiter_cli.command("create-recruiter", help="Creates a recruiter")
@click.argument('name')
@click.argument('email')
@click.argument('company_name')
def create_recruiter_command(name, email, company_name):
    create_recruiter(name, email, company_name)

@recruiter_cli.command("view-recruiter", help="Lists recruiters in the database")
@click.argument("format", default="string")
def view_recruiters_command(format):
    if format == 'string':
        print(get_all_recruiters())
    else:
        print(get_all_recruiters_json())

@recruiter_cli.command("view-applications", help="Lists of applications in the database")
@click.argument("format", default="string")
def view_application_command(format):
    if format == 'string':
        print(get_all_applications())
    else:
        print(get_all_applications_json())

@recruiter_cli.command("view-applicants", help="Lists of applicants in the database")
@click.argument("format", default="string")
def view_applicant_command(format):
    if format == 'string':
        print(get_all_applicants())
    else:
        print(get_all_applicants_json())


app.cli.add_command(recruiter_cli)

job_cli = AppGroup('job', help='Job object commands')

@job_cli.command("create-job", help="Creates a job")
@click.argument('recruiter_id')
@click.argument('job_title')
@click.argument('description')
@click.argument('salary')
@click.argument('location')
def create_job_command(recruiter_id,job_title,description, salary, location):
    create_job(recruiter_id,job_title,description, salary, location)

@job_cli.command("view-job", help="View Jobs in the database")
@click.argument("format", default="string")
def view_job_command(format):
    if format == 'string':
        print(get_all_jobs())
    else:
        print(get_all_jobs_json())

app.cli.add_command(job_cli)


applicant_cli = AppGroup('applicant', help='Applicant object commands')

@applicant_cli.command("create-applicant", help="Creates an applicant")
@click.argument('name')
@click.argument('email')
def create_applicant_command(name, email):
    create_applicant(name, email)

@applicant_cli.command("view-job", help="View Jobs in the database")
@click.argument("format", default="string")
def view_job_command(format):
    if format == 'string':
        print(get_all_jobs())
    else:
        print(get_all_jobs_json())


@applicant_cli.command("view-recruiter", help="Lists recruiters in the database")
@click.argument("format", default="string")
def view_recruiters_command(format):
    if format == 'string':
        print(get_all_recruiters())
    else:
        print(get_all_recruiters_json())

app.cli.add_command(applicant_cli)

application_cli = AppGroup('application', help='Application object commands')

@application_cli.command("Apply-job", help="Creates an applicant")
@click.argument('job_id')
@click.argument('applicant_id')
def create_application_command(job_id,applicant_id):
    create_application(job_id,applicant_id)

app.cli.add_command(application_cli)