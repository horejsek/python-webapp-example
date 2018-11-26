FROM debian:stretch-slim

LABEL version="1.0"

RUN apt-get update && apt-get -y install \
    libpq-dev \
    python3 \
    python3-dev \
    python3-pip \
    uwsgi \
    uwsgi-plugin-python3

COPY . /src
RUN cd /src && python3 setup.py install
RUN rm -rf /src

COPY docker/proxy/uwsgi.ini /var/www/webapp/proxy/uwsgi.ini

CMD ["uwsgi", "--emperor", "/var/www/webapp/proxy/"]
