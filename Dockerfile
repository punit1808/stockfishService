FROM ubuntu:22.04

# Install stockfish + python
RUN apt-get update && apt-get install -y --no-install-recommends \
        stockfish \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY server.py .

EXPOSE 8080

CMD ["python3", "server.py"]
