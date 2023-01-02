import enum

@enum.unique
class Status(enum.Enum):
    OPEN = 1
    CLOSE = 2

    