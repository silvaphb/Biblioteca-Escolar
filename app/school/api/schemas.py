from ninja import Schema
from typing import Optional
from datetime import datetime
from uuid import UUID

from app.school.application.dto import SchoolInDTO, SchoolUpdateDTO

class SchoolIn(Schema):
    name: str
    code_inep: str

    def to_dto(self):
        return SchoolInDTO(
            name=self.name,
            code_inep=self.code_inep
        )

class SchoolOut(Schema):
    id: UUID
    name: str
    code_inep: str
    created_at: datetime

    @staticmethod
    def from_domain(entity):
        return SchoolOut(
            id=entity.id,
            name=entity.name,
            code_inep=entity.code_inep,
            created_at=entity.created_at
        )

class SchoolUpdate(Schema):
    name: Optional[str] = None
    code_inep: Optional[str] = None

    def to_dto(self):
        return SchoolUpdateDTO(
            name=self.name,
            code_inep=self.code_inep
        )