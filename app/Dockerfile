FROM python:3.6.1-alpine

WORKDIR .
ADD . .
ADD app.py app.py
ADD manage.py manage.py

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN ls -la

ENTRYPOINT ["./entrypoint.sh"]
