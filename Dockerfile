FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y gcc g++ python3-dev libpq-dev libleveldb-dev && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app /app

CMD ["python", "main.py"]
