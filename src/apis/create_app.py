from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.apis.routes.user_route import router as router_user


api_router = APIRouter(prefix="/api")
api_router.include_router(router_user)


def create_app():
    app = FastAPI(
        docs_url="/",
        title="API"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
