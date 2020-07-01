import os
import sys
import json
import requests

from celery import Celery

app = Celery('worker', broker=os.getenv('RABBITMQ_URL'))


def get_access_token(api_username, api_password):
    payload = json.dumps({'username': api_username, 'password': api_password})
    token_response = requests.post(
        os.getenv('FLASK_API_ENDPOINT') + 'login',
        data=payload,
        headers={'Content-Type': 'application/json'}
    ).text
    return json.loads(token_response)['access_token']


@app.task
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


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    interval = float(os.getenv('INTERVAL'))
    urls_path = os.getenv('URLS_PATH')

    token = get_access_token('test', 'test')

    urls = []
    with open(urls_path, 'r') as f:
        urls = f.readlines()
    urls = [x.strip() for x in urls]

    print('Worker started...')

    for url in urls:
        sender.add_periodic_task(interval, check_url.s(url, token))
