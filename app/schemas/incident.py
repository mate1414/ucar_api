from datetime import datetime

from pydantic import BaseModel

from app.schemas.enums import IncidentStatus


class IncidentResponse(BaseModel):
    id: int
    description: str
    source_id: int
    status: IncidentStatus
    created_at: datetime

    class Config:
        from_attributes = True


class IncidentCreateRequest(BaseModel):
    description: str
    source_id: int

    class Config:
        from_attributes = True


class IncidentUpdateRequest(BaseModel):
    status: IncidentStatus

    class Config:
        from_attributes = True
