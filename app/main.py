from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.teacher.analytics import router as teacher_analytics_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Basic CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Teacher Domain Routers
app.include_router(
    teacher_analytics_router,
    prefix=f"{settings.API_V1_STR}/teacher",
    tags=["Teacher Analytics"],
)


@app.get("/health", tags=["Health Checks"])
async def health_check() -> dict[str, str]:
    """
    Basic health check endpoint to verify backend service status.
    """
    return {"status": "ok", "app": settings.PROJECT_NAME}

