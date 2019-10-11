"""This data is also available from the /swagger.json endpoint"""
import yaml

from flask import json

from app import app, api

with app.app_context():
    # json format
    # print(json.dumps(api.__schema__))
    # yaml format
    print(yaml.dump(api.__schema__))
