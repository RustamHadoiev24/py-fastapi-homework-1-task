from datetime import date as dt_date
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

class MovieSchema(BaseModel):
    id: int
    name: str
    release_date: dt_date = Field(validation_alias="date", serialization_alias="date")
    revenue: float
    score: float = Field(ge=0, le=100)
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: float
    country: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

class MovieListResponseSchema(BaseModel):
    movies: List[MovieSchema]
    total_pages: int
    total_items: int
    prev_page: Optional[str] = None
    next_page: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
