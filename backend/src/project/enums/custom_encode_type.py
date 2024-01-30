from enum import auto

from backend.src.project.enums import NameEnum


class CustomEncodeType(NameEnum):
    TORTOISE = auto()
    PYDANTIC = auto()
    ENUM = auto()
