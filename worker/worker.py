import os
import sys
from time import sleep
import requests
import json

if __name__ == '__main__':
	# interval = float(sys.argv[1])
	# urls_path = sys.argv[2]	

	interval = 60
	urls_path = "urls.txt"
	headers = {'Content-Type': 'application/json'}
	urls = []
	with open(urls_path, 'r') as f:
		urls = f.readlines()
	urls = [x.strip() for x in urls]

	while True:
		for url in urls:
			status = requests.get(url).status_code
			payload = json.dumps({'url': url, 'status': status})
			r = requests.post(os.getenv('STATUS_API_ENDPOINT'), data=payload, headers=headers)
		sleep(interval)

