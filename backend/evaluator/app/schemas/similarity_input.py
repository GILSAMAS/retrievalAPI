from pydantic import BaseModel


class SimpleInput(BaseModel):
    text: str
    ground_truth: str
