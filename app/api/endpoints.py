"""
Primary API route endpoints

"""
from fastapi import APIRouter
from starlette.requests import Request


# Init FastAPI router for API endpoints
api_routes = APIRouter()


@api_routes.get('/hello/{name}')
async def get_hello(request: Request, name: str = 'world'):
    return dict(hello=name)
