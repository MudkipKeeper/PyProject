FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/

RUN apt-get update
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /app

RUN chmod +x ./boot.sh
ENV FLASK_APP main.py

CMD ["./boot.sh"]