import requests

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lab3.db import Base, TODO


engine = create_engine("sqlite:///db.sqlite", echo=True)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base.metadata.create_all(engine)


query = requests.get("https://jsonplaceholder.typicode.com/todos")

print(query.json())


def save_data_to_db(query_in: requests) -> None:
    for todo in query_in.json():
        task = TODO(
            user_id=todo["userId"],
            task_id=todo["id"],
            title=todo["title"],
            completed=todo["completed"]
        )
        session.add(task)
        session.commit()


def get_data_from_db(session_in, model_in) -> list[dict]:
    stmt = session_in.query(model_in).all()
    return [
        {key: value for key, value in obj.__dict__.items() if not key.startswith("_")}
        for obj in stmt
    ]


print(get_data_from_db(session, TODO))
