from ninja import NinjaAPI
from app.book.api.views import api

app = NinjaAPI(
    title='Bibliotech', description='Eficiencia na biblioteca escolar.'
)

app.add_router('/books', api, tags=['Book'])
