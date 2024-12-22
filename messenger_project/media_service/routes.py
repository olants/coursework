from flask import Blueprint, request, jsonify
from models import db, Media
media_routes = Blueprint('media_routes', __name__)
@media_routes.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    new_media = Media(filename=file.filename, data=file.read())
    db.session.add(new_media)
    db.session.commit()
    return jsonify({'file_id': new_media.id}), 201
@media_routes.route('/download/<int:file_id>', methods=['GET'])
def download(file_id):
    media = Media.query.get(file_id)
    if media:
        return media.data, 200
    return jsonify({'error': 'File not found'}), 404