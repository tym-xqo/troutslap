FROM ubuntu:14.04
MAINTAINER tym@adops.com

RUN apt-get update && apt-get install -y \
    python \
    python-dev \
    libpq-dev \
    python-pip \
    python-psycopg2

RUN mkdir /remindbot
WORKDIR /remindbot

COPY remindbot.py /remindbot/remindbot.py
COPY send-script.py /remindbot/send-script.py
COPY cron.remindbot /etc/cron.d/remindbot
RUN chmod +x /remindbot/remindbot.py
COPY requirements.txt /remindbot/

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "remindbot.py"]