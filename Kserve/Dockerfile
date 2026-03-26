FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    kserve>=0.13 \
    torch \
    transformers \
    accelerate \
    sentencepiece

COPY model_server.py .
COPY llm/ ./llm/

ENTRYPOINT ["python", "model_server.py"]
