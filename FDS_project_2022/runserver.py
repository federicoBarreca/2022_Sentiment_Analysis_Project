"""
This script runs the FDS_project_2022 application using a development server.
"""

from os import environ
from FDS_project_2022 import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 8000
    app.run(HOST, PORT)
