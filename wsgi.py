# Vercel serverless function handler for Django
import os
import sys

# Add the project directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auka_terapias.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Get the WSGI application
application = get_wsgi_application()

# Vercel serverless function handler
def handler(event, context):
    """
    Vercel serverless function handler that wraps Django WSGI application
    """
    return application(event, context)
