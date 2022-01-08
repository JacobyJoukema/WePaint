FROM python:3.9-bullseye

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r "requirements.txt"

COPY server.py .

ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--reload"]