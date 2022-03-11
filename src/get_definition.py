import requests


def get_def(word):
    responce = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    print(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    meaningList = []

    for Homonym in range(len(responce.json())):
        meaningList += responce.json()[Homonym]["meanings"]

    return meaningList


print(get_def("shit"))