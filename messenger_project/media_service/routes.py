from flask import Blueprint, request, jsonify, Response
from models import db, Media

media_routes = Blueprint('media_routes', __name__)
@media_routes.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    # Validate input
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    new_media = Media(
        filename=file.filename,
        file_type=file.content_type,
        size=len(file.read()),  # File size in bytes
        data=file.read()       # Read binary data
    )
    db.session.add(new_media)
    db.session.commit()
    return jsonify({'file_id': new_media.id}), 201

@media_routes.route('/download/<int:file_id>', methods=['GET'])
def download(file_id):
    media = Media.query.get(file_id)
    if media:
        # Return binary data as a file download
        return Response(
            media.data,
            mimetype='application/octet-stream',
            headers={'Content-Disposition': f'attachment; filename={media.filename}'}
        )
    return jsonify({'error': 'File not found'}), 404