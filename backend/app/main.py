# from fastapi import FastAPI

# from app.core.config import settings


# app = FastAPI(
#     title=settings.app_name,
#     version="0.1.0",
#     description="AI-Powered Placement Preparation Portal",
#     debug=settings.debug,
# )


# @app.get("/health")
# async def health_check():
#     return {
#         "status": "ok",
#         "service": "ap3-backend",
#         "app": settings.app_name,
#         "environment": settings.app_env,
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.app_env,
    }