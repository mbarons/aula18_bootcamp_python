import requests

from db import Base, SessionLocal, engine
from models import Joke
from schemas import JokeSchema

Base.metadata.create_all(bind=engine)


def fetchJokeData(id: int):
    URL = f"https://official-joke-api.appspot.com/jokes/{id}"
    response = requests.get(URL)
    data = response.json()
    return JokeSchema(
        type=data["type"], setup=data["setup"], punchline=data["punchline"]
    )


def add_joke_to_db(joke_schema: JokeSchema) -> Joke:
    with SessionLocal() as db:
        db_joke = Joke(
            type=joke_schema.type,
            setup=joke_schema.setup,
            punchline=joke_schema.punchline,
        )
        db.add(db_joke)
        db.commit()
    return db_joke
