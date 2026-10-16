from fastapi import FastAPI

from app.routers import decks

app = FastAPI()
app.include_router(decks.router)


@app.get("/health")
def health():
    return {"status": "ok"}