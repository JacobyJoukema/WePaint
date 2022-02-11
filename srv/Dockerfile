FROM python:3.9-bullseye

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r "requirements.txt"

COPY server.py .
COPY database.py .

CMD uvicorn --host 0.0.0.0 --reload --factory server:main
