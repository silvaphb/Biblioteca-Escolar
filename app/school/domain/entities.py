from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

@dataclass
class SchoolEntity:
    id: UUID | None = field(default=None)
    name: str = field(default='')
    code_inep: str = field(default='')
    created_at: datetime = field(default_factory=datetime.now)

    def change_name(self, name: str):
        if name:
            self.name = name

    def change_code_inep(self, code_inep: str):
        if code_inep:
            self.code_inep = code_inep