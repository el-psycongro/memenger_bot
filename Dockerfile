FROM python:3.9-slim-buster as compile-image

COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY src /app
CMD ["python", "main.py"]
