import sys
import os

project_home = '/home/stelvorr/django_project'
venv_home = '/home/stelvorr/virtualenv/django_project/3.12'

# Activate virtualenv
activate_this = os.path.join(venv_home, 'bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set environment
sys.path.insert(0, project_home)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_project.settings')

# Start application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
