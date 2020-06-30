FROM python:3.6.1-alpine

WORKDIR .
ADD . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
