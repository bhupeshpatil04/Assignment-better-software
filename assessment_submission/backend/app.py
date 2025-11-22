
from flask import Flask, request, jsonify, abort
from uuid import uuid4

app = Flask(__name__)

# In-memory storage
# tasks: {task_id: {"comments": {comment_id: {id, text, author}}}}
tasks = {}

def get_task(task_id):
    if task_id not in tasks:
        # initialize empty task
        tasks[task_id] = {"comments": {}}
    return tasks[task_id]

@app.route("/tasks/<task_id>/comments", methods=["GET"])
def list_comments(task_id):
    task = get_task(task_id)
    comments = list(task["comments"].values())
    return jsonify(comments), 200

@app.route("/tasks/<task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json() or {}
    text = data.get("text")
    author = data.get("author", "anonymous")
    if not text:
        return jsonify({"error":"'text' is required"}), 400
    task = get_task(task_id)
    comment_id = str(uuid4())
    comment = {"id": comment_id, "text": text, "author": author}
    task["comments"][comment_id] = comment
    return jsonify(comment), 201

@app.route("/tasks/<task_id>/comments/<comment_id>", methods=["PUT"])
def edit_comment(task_id, comment_id):
    data = request.get_json() or {}
    text = data.get("text")
    if not text:
        return jsonify({"error":"'text' is required"}), 400
    task = get_task(task_id)
    if comment_id not in task["comments"]:
        return jsonify({"error":"comment not found"}), 404
    task["comments"][comment_id]["text"] = text
    return jsonify(task["comments"][comment_id]), 200

@app.route("/tasks/<task_id>/comments/<comment_id>", methods=["DELETE"])
def delete_comment(task_id, comment_id):
    task = get_task(task_id)
    if comment_id not in task["comments"]:
        return jsonify({"error":"comment not found"}), 404
    deleted = task["comments"].pop(comment_id)
    return jsonify({"deleted": deleted}), 200

if __name__ == "__main__":
    app.run(debug=True)
