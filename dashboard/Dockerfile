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
