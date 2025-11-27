# AI Document Platform

A Flask-based web application that allows users to generate, edit, and export documents (DOCX) and presentations (PPTX) with AI-assisted content generation.

## Screenshots

1. **Login Screen**

Secure user authentication using Bcrypt.

2. **Create New Project**

Define your project title, document type, and outline structure.

3. **Editor & AI Refinement**

Edit section content, generate text with AI, and refine drafts before exporting.

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
