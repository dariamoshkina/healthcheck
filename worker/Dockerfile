FROM python:3.6.1-alpine

WORKDIR .
ADD ./worker .
ADD urls.txt urls.txt

RUN apk update && apk add curl

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh" ]
