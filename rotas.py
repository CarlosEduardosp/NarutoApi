from fastapi import APIRouter
from functions import find


router = APIRouter()


@router.get("/")
def find_all():
    result = find()

    return result
