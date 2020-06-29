import sys
from time import sleep
import requests
import json

if __name__ == '__main__':
	# TODO: add check in dockerfile that flask is up
	sleep(30)
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
			r = requests.post('http://192.168.99.100:5000/status', data=payload, headers=headers)
		sleep(interval)

