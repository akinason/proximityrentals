from django.test import TestCase

import requests


def run():
    url = "http://localhost:8000/v1/main/user/57.json"
    params = {'pk': 57}
    res = requests.post()
    print(res.content)


if __name__ == '__main__':
    run()
