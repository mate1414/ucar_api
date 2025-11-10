from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository import incident, source


class RepositoryFactory:
    def __init__(self, db_session):
        self.db_session = db_session

    @property
    def incident(self):
        return incident.IncidentRepository(self.db_session)

    @property
    def source(self):
        return source.SourceRepository(self.db_session)


def get_repository_factory(db: Session = Depends(get_db)):
    return RepositoryFactory(db)
