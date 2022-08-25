FROM alpine:latest
LABEL maintainer="thomas@yager-madden.com"

RUN apk add --no-cache python3 \
    python3-dev \
    build-base

RUN mkdir /troutslap
WORKDIR /troutslap

COPY . /troutslap/

RUN pip3 install --upgrade pip gunicorn
RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "troutslap:app", "--log-file=-"]
