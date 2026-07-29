from abc import ABC, abstractmethod
from uuid import UUID
from typing import List

from app.school.domain.entities import SchoolEntity

class ISchoolRepository(ABC):
    @abstractmethod
    def save(self, school: SchoolEntity) -> SchoolEntity:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> SchoolEntity | None:
        ...

    @abstractmethod
    def list_all(self) -> List[SchoolEntity]:
        ...

    @abstractmethod
    def verify_by_name(self, name: str) -> bool:
        ...

    @abstractmethod
    def verify_by_code_inep(self, code_inep: str) -> bool:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> bool:
        ...