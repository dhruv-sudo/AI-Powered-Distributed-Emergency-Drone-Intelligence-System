from fastapi import APIRouter

router = APIRouter()

drones = []

@router.get("/drones")

def get_drones():

    return drones