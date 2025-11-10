from enum import StrEnum


class IncidentStatus(StrEnum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class SourceType(StrEnum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"
