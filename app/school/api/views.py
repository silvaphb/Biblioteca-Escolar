from django.db.transaction import atomic
from ninja import Router
from uuid import UUID

from app.school.api.dependencies import SchoolContainer
from app.school.api.schemas import SchoolIn, SchoolOut

school_router = Router()
school_container = SchoolContainer()

@school_router.post('/', response={201: SchoolOut})
@atomic
def create_school(request, data: SchoolIn):
    use_case = school_container.register_school_user_case()

    dto = data.to_dto()

    school = use_case.execute(dto)
    return SchoolOut.from_domain(school)

@school_router.get('/{id}', response={200: SchoolOut})
def get_by_id(request, id: UUID):
    use_case = school_container.return_by_id_school_use_case()

    response = use_case.execute(id)
    return 200, SchoolOut.from_domain(response)