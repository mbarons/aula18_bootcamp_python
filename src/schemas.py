from pydantic import BaseModel


class JokeSchema(BaseModel):  # contrato de dados/schema de dados/view da API
    type: str
    setup: str
    punchline: str

    class Config:
        from_attributes = (
            True  # pra comunicar com ORM depois, poder transformar JokeSchema em Joke
        )
