import requests 
import os 
from typing import Dict
from typing import Any


def make_embedding_request(payload:Dict[str, Any]):
    url = os.environ.get("OPENAI_EMBEDDING_URL")
    api_key = os.environ.get("OPENAI_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    if response.status_code != 200:
        print(response.text)
        raise Exception("Error with the request") 
    return response.json()

def build_payload(text:str)->Dict[str, str]:
    """
    Builds the payload for the request to the OpenAI API

    :param text: The text to be embedded
    :type text: str
    :return: The payload for the request
    """

    # NOTE: The model name is hard-coded here.
    # This is not a good practice.
    # We should move this to a configuration file.
    # We should also add some validation to make sure that the model name is valid.
    # We should also add some validation to make sure that the text is not empty.
    # We should also add some validation to make sure that the text is not too long.
    return {
        "input": text,
        "model": "text-embedding-ada-002",
        "encoding_format":"float",
    }
