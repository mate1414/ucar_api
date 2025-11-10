from fastapi import APIRouter, Depends

from app.crud.source import SourceCRUD
from app.repository.factory.factory import (
    RepositoryFactory,
    get_repository_factory,
)
from app.schemas.source import SourceCreateRequest, SourceResponse


router = APIRouter(prefix="/sources")


@router.post("/", response_model=SourceResponse)
def create_incident(
    incident: SourceCreateRequest,
    repo_factory: RepositoryFactory = Depends(get_repository_factory),
) -> SourceResponse:
    """
    Создать новый источник.

    returns:
        SourceResponse
    """
    return SourceCRUD(repo_factory.source).create(incident)
