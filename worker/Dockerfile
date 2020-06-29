FROM python:3.6.1-alpine
WORKDIR .
ADD . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["worker.py"]