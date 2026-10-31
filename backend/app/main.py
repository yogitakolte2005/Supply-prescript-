from fastapi import FastAPI

app = FastAPI(
    title="SupplyPrescript API",
    description="Backend API for supply-chain decision support",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to SupplyPrescript API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
