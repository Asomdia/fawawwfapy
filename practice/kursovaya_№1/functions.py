import random
import json
from classes import BasicWord

DATA_SOURCE = "config.json"

def load_random_word(path=DATA_SOURCE):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    random_choice = random.choice(data)
    basic_word = BasicWord(random_choice["word"], random_choice["subwords"])

    return basic_word


# response = requests.get(WORDS_ON_JSON_KEEPER)