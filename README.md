# healthcheck

### How to run the service
1. Put URLs for checking in urls.txt in root service directory
2. Set INTERVAL in .env.dev to desired interval between checks in seconds 
3. ```docker-compose build ```
4. ```docker-compose up ```
5. Check results at http://192.168.99.100:5000/status
