FROM python:3.9-bullseye

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r "requirements.txt"

COPY server.py .
COPY database.py .

CMD python main.py
