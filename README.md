# AI Document Platform

A Flask-based web application that allows users to generate, edit, and export documents (DOCX) and presentations (PPTX) with AI-assisted content generation.

## Screenshots

1. **Login Screen**

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/86af78a5-3e00-482f-9cf8-495d4936c370" />


2. **Create New Project**

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/e8891ca0-a110-4826-b703-0a7460b0c369" />


3. **Editor & AI Refinement**

<img width="960" height="540" alt="image" src="https://github.com/user-attachments/assets/dec39878-a9b5-4705-90af-5176ef0971cb" />

## Features

- **User Authentication:** Secure registration and login functionality.
- **Project Management:** Create multi-section projects.
- **AI Integration:** (Stubbed) Generate and refine content for specific sections.
- **Dual Export Formats:**
  - Export projects as formatted Word Documents (.docx).
  - Export projects as PowerPoint Presentations (.pptx).
- **Database:** Robust data persistence using MySQL and SQLAlchemy.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL, SQLAlchemy (ORM)
- **Frontend:** HTML5, JavaScript (Fetch API)
- **Document Processing:** python-docx, python-pptx
- **Security:** bcrypt for password hashing, flask-cors for cross-origin requests

## Installation & Setup

### Prerequisites

- Python 3.8+
- MySQL Server running locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-doc-platform.git
cd ai-doc-platform
