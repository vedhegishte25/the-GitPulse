from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from backend.db import engine, Base
from backend.config import get_settings
from backend.routers import repos, contributors, issues

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database connected and tables ready")
    yield
    await engine.dispose()
    print("Database disconnected")

app = FastAPI(
    title="GitPulse API",
    description="GitHub Analytics Dashboard API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(repos.router)
app.include_router(contributors.router)
app.include_router(issues.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to GitPulse API 🚀",
        "version": "1.0.0",
        "status": "running",
        "env": settings.app_env,
    }


@app.get("/ping")
async def ping():
    return {"ping": "pong"}