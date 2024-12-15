from typing import List 
from app.ml_core.utils import make_embedding_request
from app.ml_core.utils import build_payload

def get_embeddings(text:str)->List[float]:
    """
    Get the embeddings for a given text

    :param text: The text to be embedded
    :return: The embeddings for the text
    """
    payload = build_payload(text)
    response = make_embedding_request(payload)
    embeddings = response["data"][0]["embedding"]
    return embeddings
    

