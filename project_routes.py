from flask import Blueprint, request, jsonify
from models import Project, Section
from db import db

project_bp = Blueprint("project", __name__)

@project_bp.post("/create_project")
def create_project():
    data = request.json
    
    # --- VALIDATION FIX ---
    # Check if user_id exists and is a valid integer
    user_id = data.get("user_id")
    if not user_id or str(user_id) == "undefined":
        return jsonify({"error": "User ID is missing. Please log out and log in again."}), 400
        
    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({"error": "Invalid User ID format."}), 400
    # ----------------------

    project = Project(
        user_id=user_id,
        title=data["title"],
        doc_type=data["doc_type"],
        main_topic=data["main_topic"]
    )
    db.session.add(project)
    db.session.commit()

    # Create blank sections
    # Handle potential missing 'sections' key gracefully
    sections = data.get("sections", [])
    if isinstance(sections, str): # Handle if it came in as a string
         sections = sections.split(",")

    for s in sections:
        if s.strip(): # Only add non-empty titles
            sec = Section(project_id=project.id, title=s.strip(), content="")
            db.session.add(sec)

    db.session.commit()

    return jsonify({"project_id": project.id})


@project_bp.get("/get_project/<id>")
def get_project(id):
    sections = Section.query.filter_by(project_id=id).all()
    result = [
        {"id": s.id, "title": s.title, "content": s.content,
         "feedback": s.feedback, "comment": s.comment}
        for s in sections
    ]
    return jsonify(result)