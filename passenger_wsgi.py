import os
from realestate.wsgi import application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')
