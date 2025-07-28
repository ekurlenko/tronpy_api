from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database import create_db
from app.api.router import router as api_router

app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
def startup():
    create_db()


@app.get("/", include_in_schema=False)
def main_route():
    return RedirectResponse(url="/docs")
