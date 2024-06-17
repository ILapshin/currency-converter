from fastapi import APIRouter, status, Query
from fastapi.responses import JSONResponse
from src.external_api import get_currency_rate

router = APIRouter(
    prefix='/api/rates',
    tags=['Rates'],
)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_rate(
    base: str = Query(None, alias="from"), 
    target: str = Query(None, alias="to"), 
    value=1,
):
    rate: float = await get_currency_rate(base, target)
    result: float = round(rate * int(value), 2)
    return JSONResponse({"result": result})