from fastapi import FastAPI

from api.routes.api_routes import ApiRoutes
from core.configs.app_config import Settings

settings = Settings()
app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

router = ApiRoutes()
app.include_router(router.get_router(), prefix=settings.API_V1_STR)