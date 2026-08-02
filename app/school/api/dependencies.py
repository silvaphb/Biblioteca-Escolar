from dependency_injector import providers, containers
from app.school.infrastructure.repository import SchoolRepository
from app.school.application.use_cases import (
    RegisterSchoolUseCase,
    ReturnByIdSchoolUseCase,
    ListAllSchoolUseCase,
    UpdateSchoolUseCase,
    DeleteSchoolUseCase
)

class SchoolContainer(containers.DeclarativeContainer):
    school_repo = providers.Factory(SchoolRepository)

    register_school_user_case = providers.Factory(
        RegisterSchoolUseCase, school_repo = school_repo
    )

    return_by_id_school_use_case = providers.Factory(
        ReturnByIdSchoolUseCase, school_repo = school_repo
    )

    list_all_school_use_case = providers.Factory(
        ListAllSchoolUseCase, school_repo = school_repo
    )

    update_school_use_case = providers.Factory(
        UpdateSchoolUseCase, school_repo = school_repo
    )

    delete_school_use_case = providers.Factory(
        DeleteSchoolUseCase, school_repo = school_repo
    )