from fastapi import APIRouter
from app.schemas.similarity_input import SimpleInput
from app.dependencies.evaluation import calculate_cosine_similarity
from app.ml_core.embeddings import get_embeddings
similarity = APIRouter(tags=["similarity"])

@similarity.post("/cosine_similarity/")
async def get_cosine_similarity(data: SimpleInput):
    print(data)
    input_text = data.text
    ground_truth = data.ground_truth
    emb_input = get_embeddings(input_text)
    emb_gt = get_embeddings(ground_truth)
    similarity = calculate_cosine_similarity(emb_input, emb_gt)
    return {"similarity": similarity}

    



