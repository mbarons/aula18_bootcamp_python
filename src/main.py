import random
import time

from controller import add_joke_to_db, fetchJokeData


def main():
    while True:
        joke_id = random.randint(1, 50)
        joke_schema = fetchJokeData(joke_id)
        if joke_schema:
            print("Adicionando piada ao db.")
            add_joke_to_db(joke_schema)
        else:
            print("Não foi possível obter dados da piada.")
        time.sleep(10)


if __name__ == "__main__":
    main()
