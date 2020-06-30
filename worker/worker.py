import os
import sys
from time import sleep
import requests
import json

def get_access_token(api_username, api_password):
	payload = json.dumps({'username': api_username, 'password': api_password})
	token_response = requests.post(
		os.getenv('FLASK_API_ENDPOINT')+'login',
		data=payload,
		headers={'Content-Type': 'application/json'}
	).text
	return json.loads(token_response)['access_token']

if __name__ == '__main__':
	interval = float(sys.argv[1])
	urls_path = sys.argv[2]	

	token = get_access_token('test', 'test')
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {token}'
	}

	urls = []
	with open(urls_path, 'r') as f:
		urls = f.readlines()
	urls = [x.strip() for x in urls]

	while True:
		for url in urls:
			status = requests.get(url).status_code
			payload = json.dumps({'url': url, 'status': status})
			r = requests.post(
				os.getenv('FLASK_API_ENDPOINT')+'status', 
				data=payload, 
				headers=headers
			)
		sleep(interval)
