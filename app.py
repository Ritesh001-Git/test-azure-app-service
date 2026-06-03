from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello from Azure App Service!",
        "status": "running"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
