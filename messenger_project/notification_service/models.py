from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Notification(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        recipient = db.Column(db.String(80), nullable=False)
        message = db.Column(db.Text, nullable=False)