from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.db import SessionDepends
from src.apps.api.metadata import schemas
from src.apps.api.metadata import repositories
from src.apps.api.metadata import model

router = APIRouter(prefix="/v1")


@router.get(
    "/getFileList",
    response_model=list[schemas.StorageFile],
    summary="Get file list")
async def get_test(
    session: SessionDepends
) -> list[schemas.StorageFile]:
    pass


@router.post(
    "/addNewStorage",
    summary="Add New storage")
async def add_new_storage(
    session: SessionDepends,
    test_sq: list[schemas.Test]
) -> JSONResponse:
    if not test_sq:
        raise HTTPException(status_code=422, detail="Products list is empty")
    dto_test = model.Test(
        amount=500
    )
    await repositories.TestRepository(session).add_test_row(dto_test)
    return JSONResponse(status_code=201, content={"result": "ok"})
