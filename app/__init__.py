from flask import Flask
from flask_cors import CORS

from .routes.hello_route import hello_blueprint
from .routes.index_route import index_blueprint
from .routes.query_route import query_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(hello_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(query_blueprint)

    return app
