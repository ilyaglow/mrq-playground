FROM python:2

RUN apt-get update \
  && apt-get install -y python-dev \
                        python-pip \
                        python-lxml \
                        build-essential \
  && pip install mrq \
                 requests \
                 lxml \
  && apt-get purge -y build-essential

VOLUME /app

WORKDIR /app

CMD mrq-worker crawl
