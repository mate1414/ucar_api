from app.db.models.source import Source
from app.repository.source import SourceRepository
from app.schemas.source import SourceCreateRequest, SourceResponse


class SourceCRUD:
    def __init__(self, repository: SourceRepository):
        self.repository = repository

    def create(self, source_data: SourceCreateRequest) -> SourceResponse:
        incident = Source(
            name=source_data.name,
            description=source_data.description,
            source_type=source_data.source_type,
        )

        return SourceResponse.model_validate(self.repository.create(incident))
