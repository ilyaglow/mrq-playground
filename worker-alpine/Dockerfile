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

ENV EXAMPLE_APK_DEPS \
  py-lxml

ENV EXAMPLE_PY_DEPS \
  requests \
  lxml

RUN apk add --no-cache $EXAMPLE_APK_DEPS \
  && pip install $EXAMPLE_PY_DEPS

VOLUME /app

WORKDIR /app

CMD mrq-worker crawl
