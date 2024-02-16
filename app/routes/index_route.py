from flask import Blueprint, request, jsonify

from app.services import index_service
from app.utils import text_utils

index_blueprint = Blueprint('index', __name__, url_prefix='/api/index')


@index_blueprint.route('/', methods=['POST'])
def index_text():
    index = request.json.get('index_name')
    text = request.json.get('text')
    # Create chunks of text to index
    chunks = text_utils.split_text_semantically(text)
    # chunks = text_utils.split_long_text(text)
    for chunk in chunks:
        if chunk and len(chunk) > 0:
            index_service.index_text(text_utils.generate_unique_id(chunk), chunk, index)

    return jsonify({'message': 'Text indexed successfully'})
