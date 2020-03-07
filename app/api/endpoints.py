"""
Primary API route endpoints

"""
from fastapi import APIRouter
from starlette.responses import RedirectResponse


# Init FastAPI router for API endpoints
api_routes = APIRouter()


@api_routes.get('/')
def redirect_to_docs():
    """Redirect to API docs when at site root"""
    return RedirectResponse('/redoc')


@api_routes.get('/hello/{name}')
async def get_hello(name: str = 'world'):
    return dict(hello=name)
