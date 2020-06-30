FROM python:3.6.1-alpine
WORKDIR .
ADD . .

RUN apk update && apk add curl

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh", "python"]
