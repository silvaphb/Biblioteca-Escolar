from django.db.transaction import atomic
from ninja import Router

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