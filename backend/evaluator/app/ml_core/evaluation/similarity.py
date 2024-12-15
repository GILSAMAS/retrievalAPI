from typing import List
from sklearn.metrics.pairwise import cosine_similarity


def calculate_cosine_similarity(vector1: List[float], vector2: List[float]) -> float:
    """
    Calculates the cosine similarity between two vectors

    :param vector1: The first vector
    :param vector2: The second vector
    :return: The cosine similarity between the two vectors
    """
    return cosine_similarity([vector1], [vector2])[0][0]
