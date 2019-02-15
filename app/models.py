from app import app, db
from datetime import datetime



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    message = db.Column(db.String(200))
    time = db.Column(db.DateTime, default=datetime.now().date())
