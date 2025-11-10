from sqlalchemy.orm import Session

from app.db.models.source import Source
from app.repository.base import BaseRepository


class SourceRepository(BaseRepository):
    """
    Репозиторий для выполнения запросов к таблице 'sources'
    """

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, source: Source) -> Source:
        self.db.add(source)
        self.db.commit()

        return source
