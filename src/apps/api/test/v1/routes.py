from uuid import UUID

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.db import SessionDepends
from src.apps.api.test import schemas
from src.apps.api.test import repositories
from src.apps.api.test import model

router = APIRouter(prefix="/test")


@router.get("/", response_model=list[schemas.Test], summary="Get test sequence")
async def get_test(
    session: SessionDepends
) -> list[schemas.Test]:
    test = await repositories.TestRepository(session).get_list()
    return test


@router.post("/", summary="Add new test sequence")
async def add_new_order(
    session: SessionDepends,
    test_sq: list[schemas.Test]
) -> JSONResponse:
    if not test_sq:
        raise HTTPException(status_code=422, detail="Products list is empty")
    dto_test = model.Test(
        amount=500
    )
    await repositories.TestRepository(session).add(dto_test)
    return JSONResponse(status_code=201, content={"result": "ok"})
