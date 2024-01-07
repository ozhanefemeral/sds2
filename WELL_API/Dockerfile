FROM python:3.8-slim

WORKDIR /app

COPY WELL.c /app
COPY WELL.h /app
COPY rest-api.py /app

RUN apt-get update \
    && apt-get install -y build-essential \
    && pip install --upgrade pip \
    && pip install flask \
    && pip install flask_cors

RUN gcc -o well WELL.c -lm

EXPOSE 8080

CMD ["python", "rest-api.py"]
