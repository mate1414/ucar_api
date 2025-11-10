from pydantic import BaseModel

from app.schemas.enums import SourceType


class SourceResponse(BaseModel):
    id: int
    name: str
    description: str
    source_type: SourceType

    class Config:
        from_attributes = True


class SourceCreateRequest(BaseModel):
    name: str
    description: str
    source_type: SourceType

    class Config:
        from_attributes = True
