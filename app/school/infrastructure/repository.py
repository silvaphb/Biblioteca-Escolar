from typing import List
from uuid import UUID

from app.school.infrastructure.models import School
from app.school.domain.entities import SchoolEntity
from app.school.domain.repositories import ISchoolRepository

class SchoolRepository(ISchoolRepository):
    def save(self, school: SchoolEntity) -> SchoolEntity:
        School.objects.update_or_create(
            id=school.id,
            defaults={
                'name': school.name,
                'code_inep': school.code_inep,
                'created_at': school.created_at
            }
        )
        return school

    def find_by_id(self, id: UUID) -> SchoolEntity | None:
        try:
            return self.to_entity(School.objects.get(id=id))
        except School.DoesNotExist:
            return None

    def list_all(self) -> List[SchoolEntity]:
        return [self.to_entity(school_entity) for school_entity in School.objects.all()]

    def verify_by_name(self, name: str) -> bool:
        return School.objects.filter(name=name).exists()

    def verify_by_code_inep(self, code_inep: str) -> bool:
        return School.objects.filter(code_inep=code_inep).exists()

    def delete(self, id: UUID) -> bool:
        try:
            School.objects.get(id=id).delete()
            return True
        except School.DoesNotExist:
            return False

    def to_entity(self, model):
        return SchoolEntity(
            id=model.id,
            name=model.name,
            code_inep=model.code_inep,
            created_at=model.created_at
        )