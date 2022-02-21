import requests
from celery import shared_task
from sqlalchemy.orm import Session

from project.grades.models import Grade


@shared_task
def seed(db: Session):
    r = requests.get('https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.json')
    columns = r.json()["meta"]["view"]["columns"]
    columns_name = list(map(lambda row: row['fieldName'], columns))

    data = r.json()["data"]

    grades_dict = list(map(lambda row: {columns_name[i]: row[i] for i in range(8, len(data[0]))}, data))
    grades_objects = list(map(lambda grade_dict: Grade(**grade_dict), grades_dict))

    db.add_all(grades_objects)
    db.commit()


@shared_task
def delete(db: Session):
    print("HERE?")