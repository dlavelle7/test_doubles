"""This is also available from the /swagger.json endpoint"""
from flask import json

from app import app, api

with app.app_context():
    print(json.dumps(api.__schema__))
