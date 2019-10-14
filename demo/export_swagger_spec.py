import yaml
import requests

response = requests.get("http://localhost:5000/swagger.json")

schema_data = response.json()


def create_response_example(schema_ref):
    schema_name = schema_ref.split("#/definitions/")[1]
    # TODO: Inherit has 'allOf' property, would have to recursively call
    schema = schema_data["definitions"][schema_name]
    # TODO: What about array response types (schema 'type' property)??
    example_object = {}
    for property_name, property_data in schema.get("properties", []).items():
        example_object[property_name] = property_data["example"]
    return example_object


# Inject double module name here manually to reference connexion module
for path, methods in schema_data["paths"].items():
    for method, method_data in methods.items():
        if method not in ("get", "post", "patch", "put", "delete"):
            continue
        method_data["operationId"] = f"double.{method_data['operationId']}"
        # Set the response examples using the example values from the definintions
        for http_code, response_data in method_data.get("responses", []).items():
            schema_ref = response_data.get("schema", {}).get("$ref")
            if schema_ref is None:
                continue
            response_example = create_response_example(schema_ref)
            # TODO: Hard coding application/json (use content-type property)??
            response_data["examples"] = {"application/json": response_example}


print(yaml.dump(schema_data))
