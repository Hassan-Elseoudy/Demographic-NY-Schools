from fastapi import APIRouter

users_router = APIRouter(
    prefix="/grades",
)

from . import models, tasks # noqa