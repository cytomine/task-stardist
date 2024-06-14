FROM python:3.10.14-slim-bullseye

WORKDIR /app
COPY build/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./models/ /models
COPY scripts/run.py /app/run.py

ENTRYPOINT ["python", "run.py"]
