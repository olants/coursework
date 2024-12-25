from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    recipient = db.Column(db.String(80), nullable=False)  # Ensure this line exists
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Add timestamp
    status = db.Column(db.String(20), default='sent')  # Optional status


    def send(self):
        pass

    def receive(self):
        pass

    def mark_as_read(self):
        pass

    def delete(self):
        pass
