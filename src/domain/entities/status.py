from enum import Enum


class Status(Enum):
    NOT_STARTED = "not_started"
    STARTED = "started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABANDONED = "abandoned"
