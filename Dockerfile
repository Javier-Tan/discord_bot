FROM python:3.10.11

COPY . /app
WORKDIR /app
RUN pip install -U -r requirements.txt

CMD ["python3", "main.py"]