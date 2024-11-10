from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Cheese, Pizza, Fruit",
        "done": False
    },
    {
        "id": 2,
        "title": "Learn Python",
        "description": "Need to find a good Python tutorial on the web",
        "done": False
    }
]
# GET route to add two numbers
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world'

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify({"tasks": tasks}), 200
    

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    code = 404
    result = {"error": "Task not found"}
    for t in tasks:
        if t['id'] == task_id:
            result ={"task": t}
            code = 200
            break
    return jsonify(result), code



@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = len(tasks) + 1
    data['id'] = task_id
    data['done'] = False
    tasks.append(data)
    return jsonify(tasks), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    result = {"error": "Task not found"}
    code = 404
    for t in tasks:
        if t['id'] == task_id:
            if 'title' in data:
                t['title'] = data['title']
            if 'description' in data:
                t['description'] = data['description']
            if 'done' in data:
                t['done'] = data['done']
            result = {"task": t}
            code = 200
            break
    return jsonify(result), code

# def create_task():
#     data = request.get_json()

#     if not data or 'title' not in data or not isinstance(data['title'], str):
#         return jsonify({"error": "Bad request"}), 400
#     task_id = len(tasks) + 1
#     data['id'] = task_id
#     data['done'] = False
#     # Prepare new task data
#     new_task = {
#         'id': task_id,
#         'title': data['title'],
#         'description': data.get('description', ""),  # Use default empty string if not provided
#         'done': False  # Use True or False with capital F
#     }
#     tasks.append(new_task)
#     return jsonify({"task": new_task}), 201
# POST route for login
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()  # Retrieve JSON data from the request body
#     username = data.get('username')
#     password = data.get('password')

#     # Simple authentication check
#     if username == 'admin' and password == 'password123':
#         return jsonify({"message": "Login successful", "user": username})
#     else:
#         return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
