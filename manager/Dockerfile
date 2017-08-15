FROM alpine

RUN apk update \
  && apk add --no-cache python \
                        python-dev \
                        py-pip \
                        \
  && apk add --virtual .deps \
                       build-base \
                       linux-headers \
  && pip install mrq \
  && apk del .deps

VOLUME /app

WORKDIR /app

CMD python add_task.py
