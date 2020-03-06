"""
Primary FastPI ASGI application

"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import api_routes


def create_app():
    # Initialize FastAPI app
    application = FastAPI()

    # Enable CORS via middleware
    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    application.include_router(api_routes)

    return application


app = create_app()
