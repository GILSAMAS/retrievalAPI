from fastapi import APIRouter
from app.schemas.similarity_input import SimpleInput
from app.ml_core.embeddings import get_embeddings
from app.ml_core.evaluation.factories import SimilarityFactory

similarity = APIRouter(tags=["similarity"])


@similarity.post("/cosine_similarity/")
async def get_cosine_similarity(data: SimpleInput):
    input_text = data.text
    ground_truth = data.ground_truth

    emb_input = get_embeddings(input_text)
    emb_gt = get_embeddings(ground_truth)

    similarity = SimilarityFactory.get_similarity_metric("cosine_similarity")(
        emb_input, emb_gt
    )
    return {"similarity": similarity}
