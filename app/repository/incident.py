from typing import Sequence
from sqlalchemy.orm import Session

from app.db import models
from app.db.models.incident import Incident
from app.repository.base import BaseRepository
from app.schemas.enums import IncidentStatus


class IncidentRepository(BaseRepository):
    """
    Репозиторий для выполнения запросов к таблице 'incidents'
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def get_one(self, incident_id) -> Incident | None:
        return self.db.query(
            models.Incident
        ).filter_by(id=incident_id).one_or_none()

    def get_multi_by_status(
            self,
            status: IncidentStatus | None,
    ) -> Sequence[Incident]:
        if status is None:
            return self.db.query(models.Incident).all()

        return self.db.query(models.Incident).filter_by(status=status).all()

    def create(self, incident: Incident) -> Incident:
        self.db.add(incident)
        self.db.commit()

        return incident

    def update(self, incident: Incident) -> Incident:
        self.db.commit()
        self.db.refresh(incident)

        return incident
