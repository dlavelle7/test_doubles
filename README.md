Test Doubles [WIP]
==================

Proof of concept to see if the Swagger spec of an API could be used to create
"test doubles" using Connexion, for the purpose of mocking services in a
Microservices environment.


Demo
====

First run the demo app:

```
python demo/app.py

```

Then download its swagger spec and write to a yaml file:

```
mkdir openapi/
python demo/export_swagger_spec.py > openapi/demo_api.yaml
```

Then build and run a "test double":

```
python double.py
```
