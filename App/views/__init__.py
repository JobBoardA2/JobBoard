# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from .recruiter import recruiter_views
from .job import job_views
from .application import application_views
from .applicant import applicant_views


views = [user_views, index_views, auth_views,recruiter_views,job_views,application_views,applicant_views] 
# blueprints must be added to this list