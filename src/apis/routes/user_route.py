from fastapi import APIRouter, status, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from src.utils.logger import logger
from src.utils.redis import set_key_redis, delete_key_redis


router = APIRouter(prefix="/user", tags=["User"])