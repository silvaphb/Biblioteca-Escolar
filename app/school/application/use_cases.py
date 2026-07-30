from typing import List
from uuid import UUID

from app.school.domain.repositories import ISchoolRepository
from app.school.application.dto import SchoolInDTO, SchoolOutDTO
from app.school.domain.entities import SchoolEntity
from app.school.domain.exceptions import NotFoundSchoolException

class RegisterSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository):
        self.school_repo = school_repo

    def execute(self, school: SchoolInDTO) -> SchoolOutDTO:
        entity = SchoolEntity(
            name=school.name,
            code_inep=school.code_inep
        )
        entity = self.school_repo.save(entity)
        return SchoolOutDTO.from_domain(entity)

class ReturnByIdSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository):
        self.school_repo = school_repo

    def execute(self, id: UUID) -> SchoolOutDTO:
        school = self.school_repo.find_by_id(id)
        if not school:
            raise NotFoundSchoolException('not found school with this id')

        return SchoolOutDTO.from_domain(school)

class ListAllSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository):
        self.school_repo = school_repo

    def execute(self) -> List[SchoolOutDTO]:
        return [SchoolOutDTO.from_domain(school) for school in self.school_repo.list_all()]

class UpdateSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository):
        self.school_repo = school_repo

    def execute(self, id: UUID, dto: SchoolInDTO) -> SchoolOutDTO:
        school = self.school_repo.find_by_id(id)
        if not school:
            raise NotFoundSchoolException('not found school with this id')

        if dto.name:
            school.change_name(dto.name)

        if dto.code_inep:
            school.change_code_inep(dto.code_inep)

        school = self.school_repo.save(school)
        return SchoolOutDTO.from_domain(school)

class DeleteSchoolUseCase:
    def __init__(self, school_repo: ISchoolRepository):
        self.school_repo = school_repo

    def execute(self, id: UUID) -> SchoolOutDTO:
        school = self.school_repo.find_by_id(id)
        if not school:
            raise NotFoundSchoolException('not found school with this id')

        self.school_repo.delete(id)

        return SchoolOutDTO(
            id=school.id,
            name='DELETED SCHOOL',
            code_inep='DELETED_SCHOOL',
            created_at=school.created_at
        )