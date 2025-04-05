from fastapi import FastAPI
from app.routes import orders
from fastapi import Request
from app.logging_config import logger
from app.database import create_tables

app = FastAPI()

app.include_router(orders.router, prefix="/orders", tags=["Orders"])


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response