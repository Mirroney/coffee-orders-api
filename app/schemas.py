from pydantic import BaseModel, constr, validator
from typing import Literal

class OrderCreate(BaseModel):
    drink_name: constr(min_length=1)
    size: Literal["small", "medium", "large"]
    price: float

    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

class OrderResponse(OrderCreate):
    id: int
    status: str

    model_config = {
        "from_attributes": True
    }

