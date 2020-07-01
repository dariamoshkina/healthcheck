import os
import sys
from time import sleep
import json
import requests


def get_access_token(api_username, api_password):
    payload = json.dumps({'username': api_username, 'password': api_password})
    token_response = requests.post(
        os.getenv('FLASK_API_ENDPOINT') + 'login',
        data=payload,
        headers={'Content-Type': 'application/json'}
    ).text
    return json.loads(token_response)['access_token']


def check_url(url, token):
    status = requests.get(url).status_code
    payload = json.dumps({'url': url, 'status': status})
    r = requests.post(
        os.getenv('FLASK_API_ENDPOINT') + 'status',
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
    )


if __name__ == '__main__':
    interval = float(sys.argv[1])
    urls_path = os.getenv('URLS_PATH')

    token = get_access_token('test', 'test')

    urls = []
    with open(urls_path, 'r') as f:
        urls = f.readlines()
    urls = [x.strip() for x in urls]

    print('Worker started...')

    while True:
        for url in urls:
            check_url(url, token)
        sleep(interval)
