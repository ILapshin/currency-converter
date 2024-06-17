import aiohttp
from fastapi import HTTPException, status
from src.config import FREECURRENCYAPI_KEY


async def get_currency_rate(
        base_currency: str, 
        target_currency: str,
    ) -> float:
    """
    Возвращает текущий курс для заданной пары валют.
    """
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={FREECURRENCYAPI_KEY}&base_currency={base_currency}&target_currency={target_currency}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status != status.HTTP_200_OK:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
                result: float = await resp.json()
                return result["data"][target_currency]
        except aiohttp.ClientConnectorError:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
        