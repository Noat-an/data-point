from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.db import SessionDepends
from src.apps.api.storage import schemas
from src.apps.api.storage import repositories
from src.apps.api.storage import model

router = APIRouter()


@router.get(
    "/getOwnerInfo",
    response_model=list[schemas.Owner],
    summary="Get owned info")
async def get_owner_info(
    owner_id: str,
    session: SessionDepends
) -> list[schemas.Owner]:
    repository = await repositories.OwnerRepository(session).get_owner(owner_id)
    if not repository:
        raise HTTPException(status_code=404, detail="Owner Not found")
    return repository


@router.post(
    "/addNewOwner",
    summary="Add New owner")
async def add_new_owner(
    session: SessionDepends,
    current_user: str,
    name: str,
    email: str
) -> JSONResponse:
    if not current_user:
        raise HTTPException(status_code=422, detail="Current user is empty")
    dto_test = model.StorageOwner(
        id=current_user,
        name=name,
        email=email
    )
    await repositories.OwnerRepository(session).add_owner(dto_test)
    return JSONResponse(status_code=201, content={"result": "ok"})
