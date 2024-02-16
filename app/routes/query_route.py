from flask import Blueprint, request

from app.services import answering_service

query_blueprint = Blueprint('query', __name__, url_prefix='/api/query')


@query_blueprint.route('/', methods=['POST'])
def query():
    index_name = request.json.get('index_name')
    question = request.json.get('question')
    pre_msgs = request.json.get('pre_msgs')
    response_text = answering_service.generate_answer(question, index_name, pre_msgs)

    return response_text
