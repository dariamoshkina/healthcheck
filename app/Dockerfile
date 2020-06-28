FROM python:3.6.1-alpine
WORKDIR .
ADD . .
ADD app.py app.py
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
RUN ls -la
CMD ["app.py"]