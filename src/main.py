from fastapi import FastAPI

from src.routers import currency

app = FastAPI()

app.include_router(currency.router)
