from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class SchoolInDTO(BaseModel):
    name: str
    code_inep: str

class SchoolOutDTO(BaseModel):
    id: UUID
    name: str
    code_inep: str
    created_at: datetime

    @classmethod
    def from_domain(cls, entity):
        return cls(
            id=entity.id,
            name=entity.name,
            code_inep=entity.code_inep,
            created_at=entity.created_at
        )

class SchoolUpdateDTO(BaseModel):
    name: Optional[str] = None
    code_inep: Optional[str] = None