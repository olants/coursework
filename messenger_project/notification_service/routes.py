from flask import Blueprint, request, jsonify
from models import db, Notification
notification_routes = Blueprint('notification_routes', __name__)
@notification_routes.route('/notify', methods=['POST'])
def notify():
    data = request.json
    new_notification = Notification(recipient=data['recipient'], message=data['message'])
    db.session.add(new_notification)
    db.session.commit()
    return jsonify({'message': 'Notification sent'}), 200