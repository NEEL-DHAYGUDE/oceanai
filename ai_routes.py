from flask import Blueprint, request, jsonify
from models import Section, Project
from db import db
import os
from mistralai import Mistral

ai_bp = Blueprint("ai", __name__)
API_KEY = os.environ.get("MISTRAL_API_KEY", "PUT KEY HERE (DUE TO SECURITY I HAVE NOT PUT MINE)")
client = Mistral(api_key=API_KEY)

@ai_bp.post("/generate")
def generate():
    section_id = request.json.get("section_id")
    section = Section.query.get(section_id)
    
    if not section:
        return jsonify({"error": "Section not found"}), 404

    # Fetch project to get the main topic for context
    project = Project.query.get(section.project_id)
    context = f"Project Title: {project.title}\nMain Topic: {project.main_topic}" if project else ""

    user_prompt = f"""
    Context: {context}
    
    Task: Write detailed content for the section titled '{section.title}'.
    Make it professional and informative.
    """

    try:
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "user", "content": user_prompt},
            ]
        )
        
        generated_text = chat_response.choices[0].message.content
        
        section.content = generated_text
        db.session.commit()

        return jsonify({"content": generated_text})

    except Exception as e:
        print(f"Mistral API Error: {e}")
        return jsonify({"error": str(e)}), 500


@ai_bp.post("/refine")
def refine():
    section_id = request.json.get("section_id")
    prompt = request.json.get("prompt")
    
    section = Section.query.get(section_id)
    if not section:
        return jsonify({"error": "Section not found"}), 404

    user_prompt = f"""
    Original Content:
    {section.content}
    
    Refinement Instruction: {prompt}
    
    Task: Rewrite the content based on the instruction. Return only the rewritten text.
    """

    try:
        chat_response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "user", "content": user_prompt},
            ]
        )
        
        refined_text = chat_response.choices[0].message.content
        
        section.content = refined_text
        db.session.commit()

        return jsonify({"content": refined_text})

    except Exception as e:
        print(f"Mistral API Error: {e}")
        return jsonify({"error": str(e)}), 500
