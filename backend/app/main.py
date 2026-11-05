from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for supply-chain decision support",
    version=settings.app_version,
)


@app.get("/")
def root():
    return {"message": "Welcome to SupplyPrescript API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
