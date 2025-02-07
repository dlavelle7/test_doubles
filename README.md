# Test Doubles POC [WIP]

## Proof of Concept

Use Flask RESTPlus generated Swagger spec to build "test doubles" with
Connexion for testing Microservices

## Test Doubles

Implement 3 types of "test doubles", both defined by the actual APIs Swagger spec:

1. Test double that returns resources using the "example" values from the Swagger spec

2. Test double that returns resources based on simple and easily defined conditional logic

3. Test double that returns random resource field values based on the field type


## Demo

To demonstrate the "test doubles", I've created a demo API using Flask RESTPlus
which automatically generates Swagger API specification.

First run the demo app (to access the swagger.json endpoint):

```
python demo/app.py

```

Then download its swagger spec and write it to a yaml file:

```
mkdir openapi/
python demo/export_swagger_spec.py > openapi/demo_api.yaml
```

### Example values test double

Uses Connexion CLI to run a mock server which returns static example responses 
on every request, from the example values in the Swagger spec.

https://connexion.readthedocs.io/en/latest/cli.html

Run the "test double" using Connexion CLI with the APIs real Swagger spec:

```
connexion run openapi/demo_api.yaml --mock=all
```

Now you can hit the test double and get an example response:

```
$ curl localhost:5000/todos/1
{
  "id": 1,
  "task": "Take out the bins."
}
```

You can view the mock server swagger ui at: http://127.0.0.1:5000

Unfortunately, Flask RESTPlus does not support the Open API response examples
property, so the example values are pulled from the definitions.
See: https://github.com/noirbizarre/flask-restplus/issues/733

### Conditional test double

[TODO: Define the fixtures and the conditional logic in a simple manner]

Run the conditional test double:

```
python double.py
```

### Random values test double

[TODO]

## References

This POC is inspired by the `Mountebank` and `swagger-bank` projects.
