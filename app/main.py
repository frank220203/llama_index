from fastapi import FastAPI

from core.configs.app_config import Settings

settings = Settings()
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
