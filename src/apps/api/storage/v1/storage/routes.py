from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.db import SessionDepends
from src.apps.api.storage import schemas
from src.apps.api.storage import repositories
from src.apps.api.storage import model

router = APIRouter()


@router.get(
    "/getStorageList",
    response_model=list[schemas.StorageList],
    summary="Get a list of storage owned by the user")
async def get_storage(
    owner_id: str,
    session: SessionDepends
) -> list[schemas.StorageList]:
    repository = await repositories.RemoteStorageRepository(session).get_storage_list(owner_id)
    if not repository:
        raise HTTPException(status_code=404, detail="Storage Not found")
    return repository


@router.post(
    "/addNewStorage",
    summary="Add New storage")
async def add_new_storage(
    session: SessionDepends,
    storage_info: schemas.Storage
) -> JSONResponse:
    if not storage_info:
        raise HTTPException(status_code=422, detail="Storage info is empty")
    dto_test = model.Storage(**storage_info.model_dump())
    await repositories.RemoteStorageRepository(session).add_storage(dto_test)
    return JSONResponse(status_code=201, content={"result": "ok"})
