import os

from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='TodoMVC API',
          validate=True,
          description='A simple TodoMVC API')

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(
        readonly=True,
        description='The task unique identifier',
        example=1
    ),
    'task': fields.String(
        required=True,
        description='The task details',
        example="Take out the bins."
    )
})


class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)


DAO = TodoDAO()


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.response(200, "OK", todo)  # TODO: does this need to be a list?
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @ns.response(201, "Created", todo)
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.response(200, "OK", todo)
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        todo = DAO.get(id)
        if todo is None:
            raise NotFound

    @ns.response(204, "Deleted")
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return "", 204

    @ns.response(200, "Updated", todo)
    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)
