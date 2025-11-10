from typing import Any

from fastapi import APIRouter, Depends

from app.crud.incident import IncidentCRUD
from app.repository.factory.factory import (
    RepositoryFactory,
    get_repository_factory,
)
from app.schemas.enums import IncidentStatus
from app.schemas.incident import (
    IncidentCreateRequest,
    IncidentResponse,
    IncidentUpdateRequest,
)

router = APIRouter(prefix="/incidents")


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: int,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> IncidentResponse:
    """
    Получить информацию о инциденте по 'incident_id'.

    returns:
        IncidentResponse
    """
    return IncidentCRUD(repo_factory.incident).get_incident_or_404(incident_id)


@router.get("/", response_model=list[IncidentResponse])
def get_incidents(
    status: IncidentStatus | None = None,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> list[dict[str, Any]]:
    """
    Получить список инцидентов с фильтрацией по статусу.

    returns:
        list[IncidentResponse]
    """
    return IncidentCRUD(repo_factory.incident).get_incidents_by_status(status)


@router.post("/", response_model=IncidentResponse)
def create_incident(
    incident: IncidentCreateRequest,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> IncidentResponse:
    """
    Создать новый инцидент.

    returns:
        IncidentResponse
    """
    return IncidentCRUD(repo_factory.incident).create(incident)


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(
    incident_id: int,
    incident: IncidentUpdateRequest,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> IncidentResponse:
    """
    Обновить инцидент.

    returns:
        IncidentResponse
    """
    return IncidentCRUD(repo_factory.incident).update(incident_id, incident)
