FROM python:3.11.2-buster

WORKDIR /app
COPY . .
RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]