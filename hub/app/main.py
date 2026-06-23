from fastapi import FastAPI
app = FastAPI(title="Смета-А Hub", version="2.0.0")

@app.get("/")
async def root():
    return {"name": "Смета-А Hub", "version": "2.0.0"}

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

@app.post("/api/v1/patterns")
async def create_patterns():
    return {"accepted": 0, "rejected": 0}
