"""
Primary FastPI ASGI application

"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import api_routes


def create_app():
    # Initialize FastAPI app
    app = FastAPI()

    # Enable CORS via middleware
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_headers=['*'],
        allow_methods=['*'],
        allow_origins=['*'],
    )

    app.include_router(api_routes)

    return app


application = create_app()
