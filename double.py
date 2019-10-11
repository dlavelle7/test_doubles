import connexion

# TODO: Find a simple way of defining and returning fixtures based on conditional logic

def create_todo(*args, **kwargs):
    return {
        "id": 10,
        "task": "Do the hoovering"
    }


def delete_todo(*args, **kwargs):
    return {}


def put_todo(*args, **kwargs):
    return {
        "id": 10,
        "task": "Feed the rabbit."
    }


def get_todo(*args, **kwargs):
    return {
        "id": 10,
        "task": "Do the hoovering"
    }


def list_todos(*args, **kwargs):
    return [get_todo()]


app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('demo_api.yaml')
app.run(port=8080)
