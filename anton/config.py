import json
import os

FILE = '/default.json'
DIR = os.path.dirname(os.path.abspath(__file__))
PATH = DIR + FILE


def auth():
    config = open(PATH, 'r')
    auth = json.loads(config.read())
    return auth


if __name__ == "__main__":
    print(config())
