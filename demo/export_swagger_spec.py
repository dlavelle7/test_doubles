import yaml
import requests

response = requests.get("http://localhost:5000/swagger.json")

schema_data = response.json()

# FIXME: have to inject module name here manually to reference connexion module
for path, methods in schema_data["paths"].items():
    for method, method_data in methods.items():
        if method not in ("get", "post", "patch", "put", "delete"):
            continue
        method_data["operationId"] = f"double.{method_data['operationId']}"

print(yaml.dump(schema_data))
