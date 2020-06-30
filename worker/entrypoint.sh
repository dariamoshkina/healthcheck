#!/bin/sh

echo "Waiting for Flask..."

while true
do
	STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$STATUS_API_ENDPOINT")
	if [ $STATUS -eq 200 ]; then
		echo "Flask started"
		break
	fi
	sleep 1
done

exec "$@"