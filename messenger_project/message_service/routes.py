from flask import Blueprint, request, jsonify
from models import db, Message
message_routes = Blueprint('message_routes', __name__)
@message_routes.route('/send', methods=['POST'])
def send():
    data = request.json
    new_message = Message(sender=data['sender'], recipient=data['recipient'], content=data['content'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 201
@message_routes.route('/receive', methods=['GET'])
def receive():
    messages = Message.query.all()
    return jsonify({'messages': [{'id': m.id, 'sender': m.sender, 'recipient': m.recipient, 'content': m.content} for m in messages]}), 200
