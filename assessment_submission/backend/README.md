
# Backend (Flask) - Comments CRUD

Run locally:
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python app.py

Run tests:
pytest -q

APIs:
GET  /tasks/<task_id>/comments
POST /tasks/<task_id>/comments   { text, author? }
PUT  /tasks/<task_id>/comments/<comment_id>  { text }
DELETE /tasks/<task_id>/comments/<comment_id>
