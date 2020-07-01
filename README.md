# healthcheck

### How to run the service
1. Put URLs for checking in urls.txt in root service directory
2. ```docker-compose build ```
3. ```docker-compose up -d ```
4. ```docker-compose run worker worker.py <interval>```
5. Check results at http://192.168.99.100:5000/status
