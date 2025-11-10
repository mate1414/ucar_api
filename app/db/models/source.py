from sqlalchemy import Column, Enum, Integer, String, Text

from app.database import Base
from app.schemas import enums


class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, default="")
    source_type = Column(
        Enum(enums.SourceType, native_enum=True),
        nullable=False,
    )
