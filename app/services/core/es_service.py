import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# Load environment variables from .env file
load_dotenv()

# Set ES properties
es_host_url = os.environ.get('ES_HOST_URL')
es_username = os.environ.get('ES_USERNAME')
es_password = os.environ.get('ES_PASSWORD')

# Initialize Elasticsearch with authentication
es = Elasticsearch(
    [es_host_url],
    http_auth=(es_username, es_password)
)


def index(index, id, body, hard_refresh=False):
    if hard_refresh:
        # Index the document
        es.index(index=index, id=id, body=body)
        print("hard indexed - ", id)
    else:
        indexed = already_indexed(id, index)
        if not indexed:
            # Index the document
            es.index(index=index, id=id, body=body)
            print("indexed - ", id)
        else:
            print("already indexed - ", id)


def already_indexed(id, index):
    # Define Elasticsearch script score query
    body = {
        "size": 1,
        "query": {
            "match": {
                "_id": id
            }
        }
    }

    # Execute the query
    res = es.search(index=index, body=body)
    if res['hits']['total']['value'] > 0:
        return True
    return False


def search_embedding(index, query_embedding, num_results=10):
    try:
        # Define Elasticsearch script score query
        body = {
            "size": num_results,
            "query": {
                "script_score": {
                    "query": {
                        "match_all": {}
                    },
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                        "params": {
                            "query_vector": query_embedding
                        }
                    }
                }
            }
        }

        # Execute the query
        res = es.search(index=index, body=body)
        return res
    except Exception as e:
        print(f"Error executing search: {e}")
        return None
