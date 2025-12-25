from fastapi import FastAPI

app = FastAPI(title="VaultKey API")


@app.get("/health")
async def health():
    return {"status": "ok"}