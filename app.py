from flask import Flask, render_template
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from db import db

# Import Blueprints
from auth_routes import auth_bp
from project_routes import project_bp
from ai_routes import ai_bp
from export_routes import export_bp

app = Flask(__name__, template_folder="templates")

# Configurations
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB
db.init_app(app)

# Enable CORS
CORS(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(project_bp)
app.register_blueprint(ai_bp)
app.register_blueprint(export_bp)

# Create tables
with app.app_context():
    db.create_all()


# ----------------------
# HOME ROUTE
# ----------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")

@app.route("/new_project.html")
def new_project():
    return render_template("new_project.html")

@app.route("/editor.html")
def editor():
    return render_template("editor.html")


# Run Server
if __name__ == "__main__":
    app.run(debug=True, port=5000)
