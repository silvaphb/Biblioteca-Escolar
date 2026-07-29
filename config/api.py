from ninja import NinjaAPI
from app.book.api.views import api

app = NinjaAPI(
    title='Bibliotech',
    description='Eficiencia na biblioteca escolar.',
    docs_url='/docs/'
)

app.add_router('/books', api, tags=['Book'])
