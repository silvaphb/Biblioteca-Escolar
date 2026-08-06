from ninja import NinjaAPI

from app.book.api.views import api
from app.school.api.views import school_router

app = NinjaAPI(
    title='Bibliotech',
    description='Eficiencia na biblioteca escolar.',
    docs_url='/docs/'
)

app.add_router('/school', school_router, tags=['School'])
app.add_router('/books', api, tags=['Book'])