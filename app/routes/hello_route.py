from flask import Blueprint

hello_blueprint = Blueprint('hello', __name__)


@hello_blueprint.route('/')
@hello_blueprint.route('/hello', methods=['GET'])
def hello():
    return 'Hello from RAG Application'
