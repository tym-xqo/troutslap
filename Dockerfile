FROM python:3-slim
LABEL maintainer="thomas@yager-madden.com"

RUN mkdir /troutslap
WORKDIR /troutslap

COPY . /troutslap/

RUN python3 -m pip install --upgrade pip gunicorn
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "troutslap:app", "--log-file=-"]
