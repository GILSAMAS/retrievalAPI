from FastAPI import APIRouter
from app.schemas.similarity_input import SimpleInput

similarity = APIRouter(tags=["cosine_similarity"])

@similarity.get("/cosine_similarity")
async def get_cosine_similarity(data: SimpleInput):
    return {"message": "Cosine Similarity"}



