from flask import Flask, request, jsonify
from models.task import Task
from data import tasks as task_list

app = Flask(__name__)

tasks = task_list.tasks
task_id_control = len(tasks) 


@app.route("/tasks")
def view_all_tasks():
    task_list = [ task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods = ["GET"])
def get_task(id): 
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
    return jsonify({"message":"Não foi possível encontrar a atividade"}), 404

@app.route("/tasks", methods =["POST"])
def create_task ():
    global task_id_control
    data = request.get_json()
    
    new_task = Task(
        id=task_id_control,
        title=data["title"],
        description=data.get("description","...")
    )

    tasks.append(new_task)
    return jsonify({"message": f"A tarefa '{new_task.title}' foi adicionada com sucesso.", "id": new_task.id})

@app.route("/tasks/<int:id>", methods = ["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    print(task)
    if task == None:
        return jsonify({"message" : "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for t in tasks:
        if t.id == id:
            tasks.remove(t)
            return jsonify({"message": "Tarefa deletada com sucesso"}), 200
    return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=8000)