from fastapi import APIRouter

grades_router = APIRouter(
    prefix="/grades",
)

from . import models, tasks # noqa