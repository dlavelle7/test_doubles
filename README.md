Test Doubles [WIP]
==================

Proof of concept to see if the Swagger spec of an API could be used with Connexion
to create "test doubles", for the purpose of mocking services in a Microservices
test environment.

Test Doubles
------------

Implement 2 types of "test doubles", both defined by the actual APIs Swagger spec:

1. Test double that returns resources using the "example" values from the Swagger spec

2. Test double that returns resources based on simple and easily defined conditional logic


Demo
----

To demonstrate the "test doubles", I've created a demo API using Flask RESTPlus
which automatically generates Swagger API Documentation.

First run the demo app (to access the swagger.json endpoint):

```
python demo/app.py

```

Then download its swagger spec and write it to a yaml file:

```
mkdir openapi/
python demo/export_swagger_spec.py > openapi/demo_api.yaml
```

Example values test double
--------------------------

Uses Connexion CLI to run a mock server which returns static example responses 
on every request, from the example values in the Swagger spec.

https://connexion.readthedocs.io/en/latest/cli.html

Run the "test double" using Connexion CLI and the actual APIs Swagger spec:

```
connexion run openapi/demo_api.yaml --mock=all
```

[TODO: I don't have examples for response yet, only for resources]

Conditional test double
-----------------------

[TODO: Define the fixtures and the conditional logic in a simple manner]

Run the conditional test double:

```
python double.py
```
