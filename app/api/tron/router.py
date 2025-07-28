from fastapi import APIRouter

router = APIRouter(prefix="/tron")

@router.get("/")
def read_requests():
    return {"status": "ok"}

@router.post("/info")
def get_info_by_address(address: str):
    return {"status": "ok"}
