from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    doc_type = db.Column(db.String(10))
    main_topic = db.Column(db.Text)

class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    feedback = db.Column(db.String(50))
    comment = db.Column(db.Text)
