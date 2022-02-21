from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from project.celery_utils import create_celery
from project.database import SessionLocal, engine
from project.grades import models, schemas
from project.grades.models import Grade
from project.grades.tasks import seed, delete


def create_app() -> FastAPI:
    app = FastAPI()

    # do this before loading routes
    app.celery_app = create_celery()

    # Dependency
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # from project.grades import grades_router
    # app.include_router(grades_router)

    @app.on_event("startup")
    async def startup_event():
        seed(SessionLocal())

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/grades", response_model=list[schemas.Grade])
    def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
        return db.query(models.Grade).offset(skip).limit(limit).all()

    @app.on_event("shutdown")
    async def shutdown_event():
        delete(SessionLocal())

    return app
