"""
This file contains utility functions for text processing.
We can also use Hugging Face's transformers library for text processing. Pick the library that best suits your needs.
"""

import hashlib
import re

import spacy

# Load a spaCy model
nlp = spacy.load("en_core_web_sm")

"""
Splits a long text into sentences based on spaCy's parsing.
"""


def split_text_semantically(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Extract sentences based on spaCy's parsing
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences


"""
(Alternative) implementation of split_long_text function.
Splits a long text into chunks. If a paragraph has more than X words, it is split into sentences
and each sentence is added to a chunk. If a sentence has more than X words, it is split into chunks of X words each.
Edit this code as needed.
"""
WORDS_PER_CHUNK = 30  # Number of words per chunk; change this value as needed


def split_long_text(long_text):
    chunks = []
    long_text = remove_html_tags(long_text)
    paras = long_text.split("\n")  # Split the long string into paragraphs
    for para in paras:
        # Split the paragraph into chunks if the number of words in the paragraph is greater than words_per_chunk
        if len(para.split()) > WORDS_PER_CHUNK:
            # Split the paragraph into sentences
            sentences = para.split(".")
            temp = ""
            for sentence in sentences:
                words = sentence.split()
                print('sentence words = ' + str(len(words)))
                # Add sentences to temp until the number of words in temp is less than words_per_chunk
                if (len(words) > WORDS_PER_CHUNK):
                    for i in range(0, len(words), WORDS_PER_CHUNK):
                        chunks.append(" ".join(words[i:i + WORDS_PER_CHUNK]))
                else:
                    if len(temp.split()) < WORDS_PER_CHUNK:
                        temp += sentence + "."
                    else:
                        chunks.append(temp)
                        temp = sentence + "."  # Start a new chunk with the current sentence
        else:
            if len(para.split()) > 0:
                chunks.append(para)

    return chunks


def generate_unique_id(text):
    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()

    # Convert the text to bytes and update the hash object
    hash_object.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    unique_id = hash_object.hexdigest()

    return unique_id


def remove_html_tags(text):
    clean_text = re.sub('<.*?>', '', text)  # Remove HTML tags using regex
    return clean_text
