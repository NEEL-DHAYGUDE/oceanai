from flask import Blueprint, request, jsonify
from models import Section
from db import db

ai_bp = Blueprint("ai", __name__)

@ai_bp.post("/generate")
def generate():
    section_id = request.json["section_id"]
    section = Section.query.get(section_id)

    # FAKE AI (Replace with Gemini/OpenAI)
    generated = f"AI generated content for: {section.title}"

    section.content = generated
    db.session.commit()

    return jsonify({"content": generated})


@ai_bp.post("/refine")
def refine():
    section_id = request.json["section_id"]
    prompt = request.json["prompt"]

    section = Section.query.get(section_id)

    refined = section.content + "\n\nRefined: " + prompt
    section.content = refined
    db.session.commit()

    return jsonify({"content": refined})
