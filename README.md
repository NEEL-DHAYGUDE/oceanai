AI Document Platform

A Flask-based web application that allows users to generate, edit, and export documents (DOCX) and presentations (PPTX) with AI-assisted content generation.

Screenshots

1. Login Screen

Secure user authentication using Bcrypt.

2. Create New Project

Define your project title, document type, and outline structure.

3. Editor & AI Refinement

Edit section content, generate text with AI, and refine drafts before exporting.

Features

User Authentication: Secure registration and login functionality.

Project Management: Create multi-section projects.

AI Integration: (Stubbed) Generate and refine content for specific sections.

Dual Export Formats:

Export projects as formatted Word Documents (.docx).

Export projects as PowerPoint Presentations (.pptx).

Database: robust data persistence using MySQL and SQLAlchemy.

Tech Stack

Backend: Python, Flask

Database: MySQL, SQLAlchemy (ORM)

Frontend: HTML5, JavaScript (Fetch API)

Document Processing: python-docx, python-pptx

Security: bcrypt for password hashing, flask-cors for cross-origin requests.

Installation & Setup

Prerequisites

Python 3.8+

MySQL Server running locally

1. Clone the Repository

git clone [https://github.com/yourusername/ai-doc-platform.git](https://github.com/yourusername/ai-doc-platform.git)
cd ai-doc-platform


2. Backend Setup

Navigate to the backend folder and install dependencies:

cd backend
pip install flask flask-cors flask-sqlalchemy pymysql python-docx python-pptx bcrypt


3. Database Configuration

Open your MySQL client (Workbench, CLI, etc.).

Create a database named ai_doc_platform.

Update backend/config.py with your MySQL credentials:

MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"
MYSQL_HOST = "localhost"
MYSQL_DB = "ai_doc_platform"


4. Run the Application

Start the Flask server:

python app.py


The server will start on http://127.0.0.1:5000.

Usage Guide

Open the App: Navigate to http://127.0.0.1:5000/ in your browser.

Register/Login: Create an account or log in.

Create Project: Click "Create New Project", select DOCX or PPTX, and provide a comma-separated list of sections (e.g., "Intro, Market Analysis, Conclusion").

Edit: Use the "Generate" button to populate sections with AI text (mocked) or "Refine" to adjust content.

Export: Click "Download DOCX" or "Download PPTX" to save your work locally.

Project Structure

/
├── backend/
│   ├── app.py              # Main entry point
│   ├── config.py           # DB Config
│   ├── models.py           # SQLAlchemy Models
│   ├── routes/             # (Blueprints for Auth, AI, Project, Export)
│   └── templates/          # HTML Files (Frontend)
└── README.md
/
