FROM python:3.10.10-buster

WORKDIR /app
COPY . .
RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]