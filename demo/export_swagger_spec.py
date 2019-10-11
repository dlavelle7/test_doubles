import yaml
import requests

response = requests.get("http://localhost:5000/swagger.json")

print(yaml.dump(response.json()))
