from typing import Any

from datetime import datetime

from fastapi import HTTPException

from app.db.models.incident import Incident
from app.repository.incident import IncidentRepository
from app.schemas.enums import IncidentStatus
from app.schemas.incident import (
    IncidentCreateRequest,
    IncidentResponse,
    IncidentUpdateRequest,
)


class IncidentCRUD:
    def __init__(self, repository: IncidentRepository):
        self.repository = repository

    def create(self, incident_data: IncidentCreateRequest) -> IncidentResponse:
        incident = Incident(
            description=incident_data.description,
            status=IncidentStatus.CREATED,
            source_id=incident_data.source_id,
            created_at=datetime.now(),
        )

        return IncidentResponse.model_validate(
            self.repository.create(incident)
        )

    def update(
            self,
            incident_id: int,
            incident_data: IncidentUpdateRequest,
        ) -> IncidentResponse:
        incident_for_update = self.repository.get_one(incident_id)

        if incident_for_update is None:
            raise HTTPException(status_code=404, detail="Incident not found")

        incident_for_update.status = incident_data.status
        incident = self.repository.update(incident_for_update)

        return IncidentResponse.model_validate(
            self.repository.create(incident),
        )


    def get_incident_or_404(self, incident_id: int) -> IncidentResponse:
        incident = self.repository.get_one(incident_id)

        if incident is None:
            raise HTTPException(status_code=404, detail="Incident not found")

        return IncidentResponse.model_validate(incident)

    def get_incidents_by_status(
        self,
        status: IncidentStatus | None,
    ) -> list[dict[str, Any]]:
        incidents = self.repository.get_multi_by_status(status)

        return [
            IncidentResponse.model_validate(incident).model_dump()
            for incident in incidents
        ]
