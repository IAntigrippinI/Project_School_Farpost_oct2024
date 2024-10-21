from fastapi import FastAPI
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.api.auth import router as auth_router
from src.api.events import router as event_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(event_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
