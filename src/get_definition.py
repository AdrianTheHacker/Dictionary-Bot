import requests


def get_def(word, index):
    responce = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    print(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    meaningList = []

    for Homonym in range(len(responce.json())):
        for definition in responce.json()[Homonym]["meanings"][0]["definitions"]:
            meaningList += [definition["definition"]]

    return meaningList[index]


def get_def_num(word):
    responce = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    print(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    num = 0

    for Homonym in range(len(responce.json())):
        for definition in responce.json()[Homonym]["meanings"][0]["definitions"]:
            num += 1

    return num