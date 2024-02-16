# RAG Application using OpenAI and ElasticSearch

RAG *(Retrieval-Augmented Generation)* Application to offer Q&A on a long format text using OpenAI and
ElasticSearch. Here we are

- using ES as VectorDB to store the data and use it for search.
- using OpenAI to create embeddings and generate answers to the questions.

## Getting Started

### Prerequisites:

1. Python 3.9 or above
2. pip
3. virtualenv
4. elasticsearch (https://www.elastic.co/downloads/elasticsearch)
5. OpenAI API Key (https://platform.openai.com/)

### Installation Steps:

- Create and Activate virtual environment

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Download spacy model for NLP and splitting the text into sentences.

```bash
python -m spacy download en_core_web_sm
```

- Elasticsearch Setup (https://www.elastic.co/downloads/elasticsearch)
    1. Download and unzip Elasticsearch
    2. Start Elasticsearch `bin/elasticsearch` (or `bin\elasticsearch.bat` on Windows)
    3. Test it by running `curl -X GET "localhost:9200/"` in terminal

### Run App

Before running app, create `.env` file using `.env-template` and add OpenAI API Key and Elasticsearch credentials.

```bash
python run.py
```

App will start on `localhost` on port `8081`. Sanity check by running in terminal. It should return `Hello` message.

```bash
curl -X GET "localhost:8081"
```

## To Index and Query Data

### 1. Create ES Index

```bash
curl --location --request PUT 'http://localhost:9200/first-index' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mappings": {
        "properties": {
            "text": {
                "type": "text"
            },
            "embedding": {
                "type": "dense_vector",
                "dims": 1536
            }
        }
    }
}'
```

### 2. Index Data

To index data, use the following `curl` command. This command sends a POST request to the specified endpoint with a JSON
payload containing the text to be indexed and the name of the index.

Make sure you have the server running on `localhost` on port `8081`.

```bash
curl --location --request POST 'localhost:8081/api/index' \
--header 'Content-Type: application/json' \
--data-raw '{
  "text": "Ajeet is an engineer turned product entrepreneur with experience in AI, SaaS, HealthTech and EdTech. He is a technology enthusiast and loves to work on new technologies. He was a founding member of leading health-tech startups 1mg and HealthKart in India. He was the founder of Joe Hukum, a chatbot platform which was acquired by Freshworks. He loves solving zero to one problems and working with young and passionate engineers. Currently, he is exploring GenAI.",
  "index_name": "first-index"
}'
```

### 3. Query Data

```bash
curl --location --request POST 'localhost:8081/api/query' \
--header 'Content-Type: application/json' \
--data-raw '{
  "question": "Who is Ajeet?",
  "index_name": "first-index"
}'
```

#### Built by Ajeet with ☕️ and ❤️