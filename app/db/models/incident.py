from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.database import Base
from app.schemas import enums


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    status = Column(
        Enum(enums.IncidentStatus, native_enum=True),
        nullable=False,
    )
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    source = relationship("Source", back_populates="incidents")
