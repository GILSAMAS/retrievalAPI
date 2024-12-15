from app.ml_core.embeddings import get_embeddings
from app.dependencies.utils import calculate_cosine_similarity
from dotenv import load_dotenv


def test_get_embeddings():
    load_dotenv()
    text = "Apples are red and the sky is blue, however, the grass is green"
    text2 = "This is a test sentence that I want to use to test the embeddings"
    embeddings1 = get_embeddings(text)
    embeddings2 = get_embeddings(text2)
    similarity = calculate_cosine_similarity(embeddings1, embeddings2)
    print(similarity)
