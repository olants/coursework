# AuthService - Реєстрація та автентифікація
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'User already exists'}), 400
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(port=5000)


# MessageService - Управління повідомленнями
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    recipient = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    new_message = Message(sender=data['sender'], recipient=data['recipient'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/receive', methods=['GET'])
def receive():
    messages = Message.query.all()
    return jsonify({'messages': [{'id': m.id, 'sender': m.sender, 'recipient': m.recipient, 'content': m.content} for m in messages]}), 200

if __name__ == '__main__':
    app.run(port=5001)


# MediaService - Завантаження та обробка медіа-файлів
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db = SQLAlchemy(app)

class Media(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

db.create_all()

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    new_media = Media(filename=file.filename, data=file.read())
    db.session.add(new_media)
    db.session.commit()
    return jsonify({'file_id': new_media.id}), 201

@app.route('/download/<int:file_id>', methods=['GET'])
def download(file_id):
    media = Media.query.get(file_id)
    if media:
        return media.data, 200
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(port=5002)


# NotificationService - Сповіщення в реальному часі
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
db = SQLAlchemy(app)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    new_notification = Notification(recipient=data['recipient'], message=data['message'])
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message': 'Notification sent'}), 200

if __name__ == '__main__':
    app.run(port=5003)
