__author__ = 'Jinjia'
from app.models import Todo
from app import app
from flask.ext.script import Manager


manager = Manager(app)


@manager.command
def save():
    todo = Todo(content='Hello anthony', status=1)
    todo.save()


if __name__ == '__main__':
    manager.run()
