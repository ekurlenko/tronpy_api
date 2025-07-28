from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.api.router import router as api_router
app = FastAPI()
app.include_router(api_router)

@app.get("/", include_in_schema=False)
def main_route():
    return RedirectResponse(url="/docs")
