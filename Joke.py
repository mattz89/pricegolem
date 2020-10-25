import requests


def get_joke():
    url = 'http://api.icndb.com/jokes/random'
    joke = requests.get(url)
    joke.encoding = 'utf-8'
    data = joke.json()
    print(data['value']['joke'])