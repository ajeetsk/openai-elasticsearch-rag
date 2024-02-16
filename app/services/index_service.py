"""
Indexing service for indexing text data into Elasticsearch.
"""

from app.services.core import es_service
from app.services.core import open_ai_service


def index_text(id, text, index, hard_refresh=False):
    # Define Elasticsearch document
    body = {
        "text": text,
        "embedding": open_ai_service.generate_embedding(text)
    }

    # Index the document
    es_service.index(index, id, body, hard_refresh)
