from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    file_type = db.Column(db.String(50), nullable=False)  # Add file type
    size = db.Column(db.Float, nullable=False)            # Add file size
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.LargeBinary, nullable=False)      # Ensure this line exists

    def upload_file(self):
        pass

    def download_file(self):
        pass

    def delete_file(self):
        pass

    def rename_file(self, new_name):
        pass
