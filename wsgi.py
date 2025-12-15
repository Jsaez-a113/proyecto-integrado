"""
Vercel serverless handler for Django WSGI application
"""
import os
import sys
from io import BytesIO

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auka_terapias.settings')

# Import Django
import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler

# Create WSGI application
application = WSGIHandler()

# Vercel handler
def handler(event, context):
    """Convert Vercel event to WSGI environ and back"""
    # Build WSGI environ from Vercel event
    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'SCRIPT_NAME': '',
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', ''),
        'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
        'CONTENT_LENGTH': str(len(event.get('body', ''))),
        'SERVER_NAME': event.get('headers', {}).get('host', 'localhost'),
        'SERVER_PORT': '443',
        'SERVER_PROTOCOL': 'HTTP/1.1',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': BytesIO(event.get('body', '').encode('utf-8')),
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Add headers to environ
    for key, value in event.get('headers', {}).items():
        key = key.upper().replace('-', '_')
        if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{key}'] = value
    
    # Response holder
    response = {'statusCode': 200, 'headers': {}, 'body': ''}
    
    def start_response(status, headers, exc_info=None):
        response['statusCode'] = int(status.split()[0])
        for header, value in headers:
            response['headers'][header] = value
        return lambda s: None
    
    # Call WSGI application
    result = application(environ, start_response)
    response['body'] = b''.join(result).decode('utf-8')
    
    return response

