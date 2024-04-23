from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.db import SessionDepends
from src.apps.api.test import schemas
from src.apps.api.test import repositories
from src.apps.api.test import model

router = APIRouter(prefix="/v1")


@router.get(
    "/getTestValue",
    response_model=list[schemas.Test],
    summary="Get test sequence")
async def get_test(
    session: SessionDepends
) -> list[schemas.Test]:
    repository = await repositories.TestRepository(session).get_list()
    if not repository:
        raise HTTPException(status_code=404, detail="Not found")
    return repository


@router.post("/addTestValue", summary="Add new test sequence")
async def add_new_order(
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
