from datetime import date
from typing import Annotated, List, Optional

from pydantic import BaseModel, ConfigDict, Field
from pydantic import field_validator, model_validator


class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: Annotated[date, Field(validation_alias="release_date")]
    score: Annotated[float, Field(ge=0, le=100)]
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: int
    revenue: int
    country: str

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )

    @field_validator("revenue", mode="before")
    @classmethod
    def cast_int(cls, v):
        if v is not None:
            return int(float(v))
        return v

    @model_validator(mode='after')
    def validate_revenue(self):
        self.revenue = int(self.revenue)
        return self


class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    total_pages: int
    total_items: int
    prev_page: Optional[str] = None
    next_page: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
