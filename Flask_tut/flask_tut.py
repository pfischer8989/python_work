''' This is a flas tutorial example from here
http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

'''

from flask import Flask, jsonify
from flask import abort, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)


# JSON data that will be returned


tasks = [
    {
        'id': 1,
        'title': u'Lepous Rules',
        'description': u'Rules hard',
        'done': False

    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to learn yo',
        'done': False


    }


]






# URL target

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
# function for tasks. retrun the json data
def get_tasks():
    return jsonify({'tasks': tasks})


# function to get the id
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

# Error handler for a 404 error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'Gotta be a boolean Bro!': 'Not found'}), 404)


# POST method for adding more tasks. This adds another task to the tasks dict
# You could POST with something like this curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/todo/api/v1.0/tasks

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


# Update feature using the PUT method. Lots of error checking on format here and a check for an existing task id
# Uodate with something like this : curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:500
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


# A Delete method for removing a task
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


# translate the ID into teh URI that is called 
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

@auth.get_password
def get_password(username):
    if username == 'pfischer':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



if __name__ == '__main__':
    app.run(debug=True)

